import argparse
import importlib
import time
from bs4 import BeautifulSoup
import requests
import os


def run(year: int, day: int, part: int | None = None, test: bool = True, session: requests.Session | None = None) -> None:
    module_name = f"solutions.{year}.day{day:02d}"
    try:
        mod = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"Solution not found: {module_name}")
        return

    with open(f"inputs/{year}/day{day:02d}_{'test' if test else 'input'}.txt", "r") as f:
        input_data = f.read().strip()

    if session is None:
        session = requests.Session()
        session.cookies.set('session', os.getenv('SESSION_COOKIE'))
    soup = BeautifulSoup(
        session.get(f"https://adventofcode.com/{year}").text,
        "html.parser"
    )

    parts = [part] if part else [1, 2]
    for p in parts:
        fn = getattr(mod, f"part{p}", None)
        if fn is None:
            print(f"Part {p}: not implemented")
            continue

        start = time.perf_counter()
        result = fn(input_data)
        elapsed_ms = (time.perf_counter() - start) * 1000
        print(f"Part {p}: {result} ({elapsed_ms:.3f} ms)")

        # TODO: If the part is not solved yet, ask the user if they want to submit it

        day_element = soup.main.pre.find("a", {"href": f"/{year}/day/{day}"})
        star_data = day_element["aria-label"].removeprefix(f"Day {day}, ")

        if star_data == "two stars":
            print(f"Part {p} already solved.")

        elif star_data == "one star":
            if p == 1:
                print(f"Part {p} already solved.")
            else:
                submit = input(f"Part {p} not solved yet. Do you want to submit your answer: {result}? (y/n): ")
                if submit == "y":
                    post_answer(year, day, result, p)
        else:
            if p != 1:
                continue
            submit = input(f"Part {p} not solved yet. Do you want to submit your answer: {result}? (y/n): ")
            if submit == "y":
                post_answer(year, day, result, p, session)


def post_answer(year: int, day: int, answer: str, part: int, session: requests.Session | None = None) -> None:
    if 1 > part or 2 < part: raise ValueError(f'Can not post answer to part {part}.')
    url = f"https://adventofcode.com/{year}/day/{day}"
    if session is None:
        session = requests.Session()
        session.cookies.set('session', os.getenv('SESSION_COOKIE'))
    response = session.post(
        url + "/answer", 
        data = {'level': part, 'answer': answer}
    )
    if response.status_code != 200: 
        raise RuntimeError(f'Something went wrong when submitting answer, status code: {response.status_code}')
    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.select_one('main').text)



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