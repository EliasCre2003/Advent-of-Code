URL = None
TEST = False


def find_marker(data: str, length: int):
    chars = set()
    for i, c in enumerate(data):
        if c in chars:
            chars.clear()
        elif len(chars) == length - 1:
            return i + 1
        chars.add(c)

def part1(data: str) -> str:
    return find_marker(data, 4)

def part2(data: str) -> str:
    return find_marker(data, 14)


def load_input(test: bool = False) -> str:
    with open(f'{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    data = load_input(TEST)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()