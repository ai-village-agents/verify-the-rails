import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path

from PIL import Image


MODULE_PATH = Path(__file__).resolve().parent.parent / "tools" / "export_image_box_crops.py"
SPEC = importlib.util.spec_from_file_location("export_image_box_crops", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class ExportImageBoxCropsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.root = Path(self.temp_dir.name)

    def _make_image(
        self,
        name: str,
        color: tuple[int, int, int] = (0, 0, 0),
        size: tuple[int, int] = (48, 48),
        fmt: str = "PNG",
    ) -> Path:
        path = self.root / name
        image = Image.new("RGB", size, color)
        image.save(path, format=fmt)
        return path

    def test_parse_valid_box_spec(self) -> None:
        box = MODULE.parse_box_spec("1,2,10,20,region,#00ff00")

        self.assertEqual(1, box.x1)
        self.assertEqual(2, box.y1)
        self.assertEqual(10, box.x2)
        self.assertEqual(20, box.y2)
        self.assertEqual("region", box.label)
        self.assertEqual((0, 255, 0), box.color_rgb)

    def test_reject_malformed_box_spec(self) -> None:
        with self.assertRaisesRegex(ValueError, "Invalid --box format"):
            MODULE.parse_box_spec("1,2,3,4,label")

    def test_reject_inverted_x_coordinates(self) -> None:
        with self.assertRaisesRegex(ValueError, "x2 must be > x1"):
            MODULE.parse_box_spec("10,1,10,9,label,red")

    def test_reject_invalid_color(self) -> None:
        with self.assertRaisesRegex(ValueError, "Invalid --box color"):
            MODULE.parse_box_spec("1,2,10,20,label,not-a-color")

    def test_reject_non_integer_coordinates(self) -> None:
        with self.assertRaisesRegex(ValueError, "Invalid --box coordinates; expected integers"):
            MODULE.parse_box_spec("1,two,10,20,label,#00ff00")

    def test_reject_invalid_output_extension(self) -> None:
        input_path = self._make_image("input.png")
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            code = MODULE.main([
                str(input_path),
                "--output",
                str(self.root / "out.jpg"),
                "--box",
                "1,1,10,10,label,red",
            ])

        self.assertEqual(1, code)
        self.assertIn("must be a .png", stderr.getvalue())

    def test_reject_missing_boxes(self) -> None:
        input_path = self._make_image("input.png")
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            code = MODULE.main([
                str(input_path),
                "--output",
                str(self.root / "out.png"),
            ])

        self.assertEqual(1, code)
        self.assertIn("At least one --box is required", stderr.getvalue())

    def test_reject_negative_padding(self) -> None:
        input_path = self._make_image("input.png")
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            code = MODULE.main([
                str(input_path),
                "--output",
                str(self.root / "out.png"),
                "--box",
                "1,1,10,10,label,#00ff00",
                "--padding",
                "-1",
            ])

        self.assertEqual(1, code)
        self.assertIn("--padding must be >= 0", stderr.getvalue())

    def test_reject_nonpositive_scale(self) -> None:
        input_path = self._make_image("input.png")
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            code = MODULE.main([
                str(input_path),
                "--output",
                str(self.root / "out.png"),
                "--box",
                "1,1,10,10,label,#00ff00",
                "--scale",
                "0",
            ])

        self.assertEqual(1, code)
        self.assertIn("--scale must be > 0", stderr.getvalue())

    def test_creates_output_file_with_parent_dirs(self) -> None:
        input_path = self._make_image("input.jpg", color=(10, 10, 10), fmt="JPEG")
        output_path = self.root / "nested" / "dir" / "crops.png"

        code = MODULE.main([
            str(input_path),
            "--output",
            str(output_path),
            "--box",
            "5,5,20,20,target,#00ff00",
        ])

        self.assertEqual(0, code)
        self.assertTrue(output_path.exists())

    def test_export_contains_expected_source_color(self) -> None:
        input_path = self.root / "input.png"
        image = Image.new("RGB", (32, 32), (0, 0, 0))
        for y in range(8, 12):
            for x in range(7, 11):
                image.putpixel((x, y), (12, 34, 56))
        image.save(input_path, format="PNG")

        output_path = self.root / "sheet.png"
        code = MODULE.main([
            str(input_path),
            "--output",
            str(output_path),
            "--box",
            "6,7,12,13,target,#00ff00",
            "--padding",
            "0",
            "--scale",
            "2",
        ])

        self.assertEqual(0, code)
        with Image.open(output_path) as result:
            pixels = list(result.getdata())

        self.assertIn((12, 34, 56), pixels)


if __name__ == "__main__":
    unittest.main()
