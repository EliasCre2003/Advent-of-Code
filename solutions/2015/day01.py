
TEST = True


def part1(data: str) -> str:
    floor = 0
    for d in data:
        match d:
            case '(':
                floor += 1
            case ')':
                floor -= 1
    return floor


def part2(data: str) -> str:
    floor = 0
    for i, d in enumerate(data):
        match d:
            case '(':
                floor += 1
            case ')':
                floor -= 1
        if floor == -1:
            return i + 1


def load_input(test: bool = False) -> str:
    with open(f'solutions/2015/day01_{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    data = load_input(TEST)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
