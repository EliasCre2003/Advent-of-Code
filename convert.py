from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
SOLUTIONS_DIR = ROOT / "solutions"
INPUTS_DIR = ROOT / "inputs"
EXTRA_SOLUTIONS_DIR = ROOT / "extra_solutions"
SOURCE_EXTENSIONS = {".py", ".rs"}


def main() -> None:
    moves: list[tuple[Path, Path]] = []
    multiple_solutions: list[tuple[str, int, list[Path]]] = []

    for year_dir in sorted(ROOT.iterdir()):
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue

        year = year_dir.name

        for day_dir in sorted(year_dir.iterdir()):
            if not day_dir.is_dir():
                continue

            match = re.match(r"^(\d+)\.", day_dir.name)
            if not match:
                continue

            day = int(match.group(1))
            source_files = sorted(
                path
                for path in day_dir.rglob("*")
                if path.is_file() and path.suffix.lower() in SOURCE_EXTENSIONS
            )

            solution_file = SOLUTIONS_DIR / year / f"day{day:02}.py"
            if solution_file.is_file():
                source_files.append(solution_file)

            extra_day_dir = EXTRA_SOLUTIONS_DIR / year / f"day{day:02}"
            source_files.extend(
                path
                for path in extra_day_dir.rglob("*")
                if path.is_file() and path.suffix.lower() in SOURCE_EXTENSIONS
            )
            source_files = sorted(set(source_files))

            if len(source_files) > 1:
                multiple_solutions.append((year, day, source_files))

            main_file = day_dir / "main.py"
            if main_file.is_file():
                moves.append((main_file, solution_file))

            for filename, suffix in (("input.txt", "input"), ("test.txt", "test")):
                input_file = day_dir / filename
                if input_file.is_file():
                    target = INPUTS_DIR / year / f"day{day:02}_{suffix}.txt"
                    moves.append((input_file, target))

            handled_files = {
                main_file,
                day_dir / "input.txt",
                day_dir / "test.txt",
            }
            for extra_file in sorted(day_dir.rglob("*")):
                if extra_file.is_file() and extra_file not in handled_files:
                    target = extra_day_dir / extra_file.relative_to(day_dir)
                    moves.append((extra_file, target))

    if multiple_solutions:
        print("Days with more than one solution source:")
        for year, day, files in multiple_solutions:
            paths = ", ".join(str(path.relative_to(ROOT)) for path in files)
            print(f"  {year} day {day:02}: {paths}")
    else:
        print("No days with multiple solution sources found.")

    # Check all destinations before moving anything.
    targets: set[Path] = set()
    conflicts: list[str] = []
    for source, target in moves:
        if target.exists() or target in targets:
            conflicts.append(f"{source.relative_to(ROOT)} -> {target.relative_to(ROOT)}")
        targets.add(target)

    if conflicts:
        raise FileExistsError("Destination conflicts:\n  " + "\n  ".join(conflicts))

    for source, target in moves:
        target.parent.mkdir(parents=True, exist_ok=True)
        source.rename(target)
        print(f"Moved {source.relative_to(ROOT)} -> {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()