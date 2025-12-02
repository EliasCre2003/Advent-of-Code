TEST = False

def load_input(test: bool = False) -> str:
    with open(f'{"test" if test else "input"}.txt', 'r') as f:
        return f.read().strip()

def parse_line(line: str) -> tuple[tuple[int, int], tuple[int, int]]:
    p1, p2 = line.split(',')
    p1, p2 = p1.split('-'), p2.split('-')
    return (int(p1[0]), int(p1[1])), (int(p2[0]), int(p2[1]))

def part1(pairs: list[tuple[tuple[int, int], tuple[int, int]]]) -> str:
    total = 0
    for pair in pairs:
        p1, p2 = pair
        if ((p1[0] <= p2[0] and p1[1] >= p2[1]) or
            (p2[0] <= p1[0] and p2[1] >= p1[1])):
            total += 1
    return total


def part2(pairs: list[tuple[tuple[int, int], tuple[int, int]]]) -> str:
    total = 0
    for pair in pairs:
        p1, p2 = pair
        if ((p2[0] <= p1[0] <= p2[1]) or (p2[0] <= p1[1] <= p2[1]) or
            (p1[0] <= p2[0] <= p1[1]) or (p1[0] <= p2[1] <= p1[1])):
            total += 1
    return total


def main():
    data = load_input(TEST)
    lines = data.split('\n')
    pairs = list(map(parse_line, lines))
    print(part1(pairs))
    print(part2(pairs))

if __name__ == '__main__':
    main()