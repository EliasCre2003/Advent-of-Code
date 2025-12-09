URL = None
TEST = False


def rect_size(tile1: tuple[int, int], tile2: tuple[int, int]) -> int:
    dx = abs(tile1[0] - tile2[0]) + 1
    dy = abs(tile1[1] - tile2[1]) + 1
    return dx * dy


def to_tiles(data: str) -> list[tuple[int, int]]:
    return [
        tuple(map(int, box)) for box in
        map(lambda x: x.split(','), data.splitlines())
    ]


def part1(data: str) -> str:
    tiles = to_tiles(data)
    return max(
        rect_size(tile1, tile2)
        for i, tile1 in enumerate(tiles)
        for tile2 in tiles[(i+1):]
    )

def part2(data: str) -> str:
    ...


def load_input(test: bool = False) -> str:
    with open(f'{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    data = load_input(TEST)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()