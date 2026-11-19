import argparse
import importlib
import time


def run(year: int, day: int, part: int | None = None, test: bool = True) -> None:
    module_name = f"solutions.{year}.day{day:02d}"
    try:
        mod = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"Solution not found: {module_name}")
        return

    with open(f"inputs/{year}/day{day:02d}_{'test' if test else 'input'}.txt", "r") as f:
        input_data = f.read().strip()

    parts = [part] if part else [1, 2]
    for p in parts:
        fn = getattr(mod, f"part{p}", None)
        if fn is None:
            print(f"Part {p}: not implemented")
            continue

        start = time.perf_counter()
        result = fn(input_data)
        elapsed_ms = (time.perf_counter() - start) * 1000
        print(f"Part {p}: {result} ({elapsed_ms:.2f} ms)")

        # TODO: If the part is not solved yet, ask the user if they want to submit it
        

def main():
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
    parser.add_argument("year", type=int)
    parser.add_argument("day", type=int)
    parser.add_argument("-p", "--part", type=int, choices=[1, 2], default=None)
    parser.add_argument("-t", "--test", action="store_true", help="Run using test data")
    args = parser.parse_args()

    run(args.year, args.day, args.part, args.test)

if __name__ == "__main__":
    main()