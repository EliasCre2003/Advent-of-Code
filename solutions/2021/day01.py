URL = None
TEST = False


def part1(data: str) -> str:
    lines = list(map(int, data.splitlines()))
    prev_measurement = lines[0]
    total = 0
    for measurement in lines:
        if measurement > prev_measurement:
            total += 1
        prev_measurement = measurement
    return total


def part2(data: str) -> str:
    lines = list(map(int, data.splitlines()))
    generate_window = lambda i: sum(lines[i:i+3])
    prev_window = generate_window(0)
    total = 0
    for i in range(1, len(lines)-2):
        window = generate_window(i)
        if window > prev_window:
            total += 1
        prev_window = window
    return total


def load_input(test: bool = False) -> str:
    with open(f'{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    data = load_input(TEST)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()