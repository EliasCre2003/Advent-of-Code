def generate_template(year: int, day: int) -> str:
    return """
TEST = True


def part1(data: str) -> str:
    ...


def part2(data: str) -> str:
    ...


def load_input(test: bool = False) -> str:
    with open(f'inputs/year/day_{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    data = load_input(TEST)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
""".replace("year", str(year)).replace("day", f"day{day:02d}")


if __name__ == "__main__":
    print(generate_template(2015, 1))