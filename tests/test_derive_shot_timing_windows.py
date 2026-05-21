import contextlib
import importlib.util
import io
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path


MODULE_PATH = (
    Path(__file__).resolve().parent.parent
    / "tools"
    / "derive_shot_timing_windows.py"
)
SPEC = importlib.util.spec_from_file_location("derive_shot_timing_windows", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class DeriveShotTimingWindowsTests(unittest.TestCase):
    def _write_csv(self, content: str, *, filename: str = "SHOT_TIMINGS.csv") -> Path:
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)
        path = Path(temp_dir.name) / filename
        path.write_text(content, encoding="utf-8")
        return path

    def test_read_timing_rows_derives_cumulative_windows(self) -> None:
        csv_path = self._write_csv(
            "frame,duration_seconds\n"
            "01_title_card.png,1.5\n"
            "02_hook.png,2.0\n"
            "03_close.png,0.5\n"
        )

        rows = MODULE.read_timing_rows(csv_path)

        self.assertEqual(3, len(rows))
        self.assertEqual(1, rows[0].shot_number)
        self.assertEqual(0.0, rows[0].start)
        self.assertEqual(1.5, rows[0].end)
        self.assertEqual(2, rows[1].shot_number)
        self.assertEqual(1.5, rows[1].start)
        self.assertEqual(3.5, rows[1].end)
        self.assertEqual(3, rows[2].shot_number)
        self.assertEqual(3.5, rows[2].start)
        self.assertEqual(4.0, rows[2].end)

    def test_filter_rows_applies_focus_shots(self) -> None:
        csv_path = self._write_csv(
            "frame,duration_seconds\n"
            "01_title_card.png,1.0\n"
            "02_hook.png,1.0\n"
            "03_close.png,1.0\n"
        )
        rows = MODULE.read_timing_rows(csv_path)

        focused = MODULE.filter_rows(rows, {2, 3})
        unfocused = MODULE.filter_rows(rows, None)

        self.assertEqual([2, 3], [row.shot_number for row in focused])
        self.assertEqual([1, 2, 3], [row.shot_number for row in unfocused])

    def test_print_appendix_formatting(self) -> None:
        csv_path = self._write_csv(
            "frame,duration_seconds\n"
            "01_title_card.png,1.0\n"
            "02_hook.png,2.5\n"
        )
        rows = MODULE.read_timing_rows(csv_path)

        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            MODULE.print_appendix(rows)

        output = stdout.getvalue()
        self.assertIn("\nAppendix:\n", output)
        self.assertIn(
            "- Shot 1 (`01_title_card.png`): `0:00.0–0:01.0` (1.0s)",
            output,
        )
        self.assertIn("- Shot 2 (`02_hook.png`): `0:01.0–0:03.5` (2.5s)", output)

    def test_read_timing_rows_rejects_invalid_header(self) -> None:
        csv_path = self._write_csv(
            "frame,duration\n"
            "01_title_card.png,1.0\n"
        )

        with self.assertRaisesRegex(ValueError, "Invalid CSV header"):
            MODULE.read_timing_rows(csv_path)

    def test_read_timing_rows_rejects_nonpositive_duration(self) -> None:
        csv_path = self._write_csv(
            "frame,duration_seconds\n"
            "01_title_card.png,0\n"
        )

        with self.assertRaisesRegex(ValueError, "duration_seconds must be positive"):
            MODULE.read_timing_rows(csv_path)

    def test_read_timing_rows_rejects_filename_without_numeric_prefix(self) -> None:
        csv_path = self._write_csv(
            "frame,duration_seconds\n"
            "title_card.png,1.0\n"
        )

        with self.assertRaisesRegex(ValueError, "must start with a numeric shot prefix"):
            MODULE.read_timing_rows(csv_path)

    def test_parse_args_rejects_nonpositive_focus_shots(self) -> None:
        stderr = io.StringIO()
        with mock.patch.object(
            sys,
            "argv",
            [
                "derive_shot_timing_windows.py",
                "--timings",
                "SHOT_TIMINGS.csv",
                "--focus-shots",
                "0",
            ],
        ):
            with contextlib.redirect_stderr(stderr):
                with self.assertRaises(SystemExit) as exc:
                    MODULE.parse_args()

        self.assertEqual(2, exc.exception.code)
        self.assertIn("usage:", stderr.getvalue())
        self.assertIn("invalid positive int value: '0'", stderr.getvalue())

    def test_main_errors_when_all_requested_focus_shots_are_missing(self) -> None:
        csv_path = self._write_csv(
            "frame,duration_seconds\n"
            "01_title_card.png,1.0\n"
            "02_hook.png,1.0\n"
        )
        stdout = io.StringIO()
        stderr = io.StringIO()
        with mock.patch.object(
            sys,
            "argv",
            [
                "derive_shot_timing_windows.py",
                "--timings",
                str(csv_path),
                "--focus-shots",
                "10",
                "11",
            ],
        ):
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                exit_code = MODULE.main()

        self.assertEqual(1, exit_code)
        self.assertEqual("", stdout.getvalue())
        self.assertIn("Error:", stderr.getvalue())
        self.assertIn("Requested: [10, 11]", stderr.getvalue())
        self.assertIn("Missing: [10, 11]", stderr.getvalue())
        self.assertIn("Available: [1, 2]", stderr.getvalue())

    def test_main_errors_when_any_requested_focus_shots_are_missing(self) -> None:
        csv_path = self._write_csv(
            "frame,duration_seconds\n"
            "01_title_card.png,1.0\n"
            "02_hook.png,1.0\n"
            "03_close.png,1.0\n"
        )
        stdout = io.StringIO()
        stderr = io.StringIO()
        with mock.patch.object(
            sys,
            "argv",
            [
                "derive_shot_timing_windows.py",
                "--timings",
                str(csv_path),
                "--focus-shots",
                "2",
                "9",
            ],
        ):
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                exit_code = MODULE.main()

        self.assertEqual(1, exit_code)
        self.assertEqual("", stdout.getvalue())
        self.assertIn("Error:", stderr.getvalue())
        self.assertIn("Requested: [2, 9]", stderr.getvalue())
        self.assertIn("Missing: [9]", stderr.getvalue())
        self.assertIn("Available: [1, 2, 3]", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
