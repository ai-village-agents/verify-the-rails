import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path

from PIL import Image


MODULE_PATH = Path(__file__).resolve().parent.parent / "tools" / "compare_image_box_crops.py"
SPEC = importlib.util.spec_from_file_location("compare_image_box_crops", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class CompareImageBoxCropsTests(unittest.TestCase):
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

    def test_reject_non_integer_coordinates(self) -> None:
        with self.assertRaisesRegex(ValueError, "Invalid --box coordinates; expected integers"):
            MODULE.parse_box_spec("1,two,10,20,label,#00ff00")

    def test_reject_invalid_color(self) -> None:
        with self.assertRaisesRegex(ValueError, "Invalid --box color"):
            MODULE.parse_box_spec("1,2,10,20,label,not-a-color")

    def test_reject_missing_second_input(self) -> None:
        input_a = self._make_image("a.png")
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            code = MODULE.main([
                str(input_a),
                "--output",
                str(self.root / "out.png"),
                "--box",
                "1,1,10,10,label,#00ff00",
            ])

        self.assertEqual(1, code)
        self.assertIn("At least two input images are required", stderr.getvalue())

    def test_reject_invalid_output_extension(self) -> None:
        input_a = self._make_image("a.png")
        input_b = self._make_image("b.png")
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            code = MODULE.main([
                str(input_a),
                str(input_b),
                "--output",
                str(self.root / "out.jpg"),
                "--box",
                "1,1,10,10,label,#00ff00",
            ])

        self.assertEqual(1, code)
        self.assertIn("must be a .png", stderr.getvalue())

    def test_reject_missing_boxes(self) -> None:
        input_a = self._make_image("a.png")
        input_b = self._make_image("b.png")
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            code = MODULE.main([
                str(input_a),
                str(input_b),
                "--output",
                str(self.root / "out.png"),
            ])

        self.assertEqual(1, code)
        self.assertIn("At least one --box is required", stderr.getvalue())

    def test_reject_negative_padding(self) -> None:
        input_a = self._make_image("a.png")
        input_b = self._make_image("b.png")
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            code = MODULE.main([
                str(input_a),
                str(input_b),
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
        input_a = self._make_image("a.png")
        input_b = self._make_image("b.png")
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            code = MODULE.main([
                str(input_a),
                str(input_b),
                "--output",
                str(self.root / "out.png"),
                "--box",
                "1,1,10,10,label,#00ff00",
                "--scale",
                "0",
            ])

        self.assertEqual(1, code)
        self.assertIn("--scale must be > 0", stderr.getvalue())

    def test_reject_nonpositive_font_size(self) -> None:
        input_a = self._make_image("a.png")
        input_b = self._make_image("b.png")
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            code = MODULE.main([
                str(input_a),
                str(input_b),
                "--output",
                str(self.root / "out.png"),
                "--box",
                "1,1,10,10,label,#00ff00",
                "--font-size",
                "0",
            ])

        self.assertEqual(1, code)
        self.assertIn("--font-size must be > 0", stderr.getvalue())

    def test_creates_output_file_with_parent_dirs(self) -> None:
        input_a = self._make_image("a.jpg", color=(10, 10, 10), fmt="JPEG")
        input_b = self._make_image("b.png", color=(20, 20, 20), fmt="PNG")
        output_path = self.root / "nested" / "dir" / "compare.png"

        code = MODULE.main([
            str(input_a),
            str(input_b),
            "--output",
            str(output_path),
            "--box",
            "5,5,20,20,target,#00ff00",
        ])

        self.assertEqual(0, code)
        self.assertTrue(output_path.exists())

    def test_export_contains_expected_source_colors_from_multiple_inputs(self) -> None:
        input_a = self.root / "frame_a.png"
        input_b = self.root / "frame_b.png"

        image_a = Image.new("RGB", (24, 24), (0, 0, 0))
        image_b = Image.new("RGB", (24, 24), (0, 0, 0))
        for y in range(8, 12):
            for x in range(8, 12):
                image_a.putpixel((x, y), (200, 10, 10))
                image_b.putpixel((x, y), (10, 200, 10))
        image_a.save(input_a, format="PNG")
        image_b.save(input_b, format="PNG")

        output_path = self.root / "sheet.png"
        code = MODULE.main([
            str(input_a),
            str(input_b),
            "--output",
            str(output_path),
            "--box",
            "8,8,12,12,target,#00ff00",
            "--padding",
            "0",
            "--scale",
            "2",
        ])

        self.assertEqual(0, code)
        with Image.open(output_path) as result:
            pixels = list(result.getdata())

        self.assertIn((200, 10, 10), pixels)
        self.assertIn((10, 200, 10), pixels)


if __name__ == "__main__":
    unittest.main()
