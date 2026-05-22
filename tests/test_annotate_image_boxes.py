import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path

from PIL import Image


MODULE_PATH = Path(__file__).resolve().parent.parent / "tools" / "annotate_image_boxes.py"
SPEC = importlib.util.spec_from_file_location("annotate_image_boxes", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class AnnotateImageBoxesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.root = Path(self.temp_dir.name)

    def _make_image(
        self,
        name: str,
        color: tuple[int, int, int] = (0, 0, 0),
        size: tuple[int, int] = (40, 40),
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

    def test_reject_inverted_coords(self) -> None:
        with self.assertRaisesRegex(ValueError, "x2 must be > x1"):
            MODULE.parse_box_spec("10,1,10,9,label,red")

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

    def test_reject_invalid_color(self) -> None:
        with self.assertRaisesRegex(ValueError, "Invalid --box color"):
            MODULE.parse_box_spec("1,2,10,20,label,not-a-color")

    def test_creates_output_file_with_parent_dirs(self) -> None:
        input_path = self._make_image("input.jpg", color=(9, 9, 9), fmt="JPEG")
        output_path = self.root / "nested" / "dir" / "annotated.png"

        code = MODULE.main([
            str(input_path),
            "--output",
            str(output_path),
            "--box",
            "5,5,20,20,target,#00ff00",
        ])

        self.assertEqual(0, code)
        self.assertTrue(output_path.exists())

    def test_annotation_changes_expected_pixels(self) -> None:
        input_path = self._make_image("input.png", color=(0, 0, 0), size=(50, 50))
        output_path = self.root / "out.png"

        code = MODULE.main([
            str(input_path),
            "--output",
            str(output_path),
            "--box",
            "5,5,20,20,label,red",
            "--line-width",
            "1",
            "--font-size",
            "14",
        ])

        self.assertEqual(0, code)
        with Image.open(output_path) as result:
            self.assertEqual((255, 0, 0), result.getpixel((5, 5)))
            self.assertEqual((0, 0, 0), result.getpixel((35, 35)))


if __name__ == "__main__":
    unittest.main()
