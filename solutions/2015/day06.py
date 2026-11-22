from math import sqrt

TEST = True


def lights_in_square(x1: int, y1: int, x2: int, y2: int) -> int:
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def part1(data: str) -> str:
    ...


def part2(data: str) -> str:
    ...


def load_input(test: bool = False) -> str:
    with open(f'inputs/2015/day06_{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    data = load_input(TEST)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
