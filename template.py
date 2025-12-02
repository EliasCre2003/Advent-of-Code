TEST = True

def load_input(test: bool = False) -> str:
    with open(f'{"test" if test else "input"}.txt', 'r') as f:
        return f.read().strip()


def part1() -> str:
    ...


def part2() -> str:
    ...


def main():
    data = load_input(TEST)


if __name__ == '__main__':
    main()