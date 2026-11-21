
TEST = True


def part1(data: str) -> str:
    total = 0
    for line in data.splitlines():
        l, w, h = map(int, line.split('x'))
        faces = l*w, w*h, h*l
        total += 2 * sum(faces) + min(faces)
    return total


def part2(data: str) -> str:
    total = 0
    for line in data.splitlines():
        l, w, h = map(int, line.split('x'))
        faces = (l,w), (w,h), (h,l)
        perimeters = list(map(lambda f: 2 * (f[0] + f[1]), faces))
        total += min(perimeters) + l * w * h
    return total


def load_input(test: bool = False) -> str:
    with open(f'inputs/2015/day02_{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    data = load_input(TEST)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
