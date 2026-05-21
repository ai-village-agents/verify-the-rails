import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path

from PIL import Image


MODULE_PATH = (
    Path(__file__).resolve().parent.parent
    / "tools"
    / "make_legibility_mosaic.py"
)
SPEC = importlib.util.spec_from_file_location("make_legibility_mosaic", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class MakeLegibilityMosaicTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.root = Path(self.temp_dir.name)

    def _make_png(self, name: str, color: tuple[int, int, int], size: tuple[int, int]) -> Path:
        path = self.root / name
        image = Image.new("RGB", size, color)
        image.save(path, format="PNG")
        return path

    def test_explicit_paths_are_sorted_lexicographically(self) -> None:
        red = self._make_png("b_frame.png", (255, 0, 0), (20, 20))
        green = self._make_png("a_frame.png", (0, 255, 0), (20, 20))
        blue = self._make_png("c_frame.png", (0, 0, 255), (20, 20))
        output = self.root / "out.png"

        MODULE.make_mosaic(
            [str(red), str(green), str(blue)],
            input_dir=None,
            glob_pattern="*.png",
            output=str(output),
            columns=2,
            cell_width=20,
            cell_height=20,
            margin=0,
            gap=0,
            bg_color="#000000",
            label_height=0,
        )

        with Image.open(output) as result:
            # Sorted names: a_frame (green), b_frame (red), c_frame (blue)
            self.assertEqual((0, 255, 0), result.getpixel((10, 10)))
            self.assertEqual((255, 0, 0), result.getpixel((30, 10)))
            self.assertEqual((0, 0, 255), result.getpixel((10, 30)))

    def test_input_dir_glob_mode_filters_and_sorts(self) -> None:
        self._make_png("b_frame.png", (255, 0, 0), (10, 10))
        self._make_png("a_frame.png", (0, 255, 0), (10, 10))
        (self.root / "ignore.txt").write_text("x", encoding="utf-8")

        paths = MODULE.resolve_input_paths([], str(self.root), "*.png")

        self.assertEqual(["a_frame.png", "b_frame.png"], [path.name for path in paths])

    def test_zero_input_failure(self) -> None:
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            code = MODULE.main([
                "--input-dir",
                str(self.root),
                "--output",
                str(self.root / "out.png"),
            ])

        self.assertEqual(1, code)
        self.assertIn("No input images found", stderr.getvalue())

    def test_non_png_output_rejected(self) -> None:
        frame = self._make_png("a_frame.png", (1, 2, 3), (10, 10))
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            code = MODULE.main([
                str(frame),
                "--output",
                str(self.root / "out.jpg"),
            ])

        self.assertEqual(1, code)
        self.assertIn("must be a .png", stderr.getvalue())

    def test_expected_output_dimensions(self) -> None:
        a = self._make_png("a.png", (10, 20, 30), (40, 20))
        b = self._make_png("b.png", (40, 50, 60), (20, 40))
        c = self._make_png("c.png", (70, 80, 90), (30, 30))
        out = self.root / "nested" / "sheet.png"

        MODULE.make_mosaic(
            [str(c), str(a), str(b)],
            input_dir=None,
            glob_pattern="*.png",
            output=str(out),
            columns=2,
            cell_width=32,
            cell_height=18,
            margin=4,
            gap=2,
            bg_color="#111111",
            label_height=10,
        )

        with Image.open(out) as result:
            self.assertEqual((74, 66), result.size)


if __name__ == "__main__":
    unittest.main()
