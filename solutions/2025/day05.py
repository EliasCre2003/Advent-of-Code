TEST = False


def parse_data(data: str) -> tuple[tuple[int, int], list[int]]:
    range_str, ing_str = data.split('\n\n')
    ranges = [tuple(map(int, line.split('-'))) for line in range_str.splitlines()]
    ingredients = [int(line) for line in ing_str.splitlines()]
    return ranges, ingredients


def part1(data: str) -> str:
    ranges, ingredients = parse_data(data)
    def is_fresh(ingredient: int) -> bool:
        for range in ranges:
            if range[0] <= ingredient <= range[1]:
                return True
        return False
    return sum(map(is_fresh, ingredients))


def part2(data: str) -> str:
    ranges, _ = parse_data(data)

    def fix_overlap(range1: tuple[int, int]) -> tuple[int, int]:
        new_range = list(range1)
        for range2 in ranges:
            if range2 is None: continue
            if range2 == range1: continue
            if range2[0] <= new_range[0] and range2[1] >= new_range[1]:
                return None
            if range2[0] <= new_range[0] and new_range[0] <= range2[1] <= new_range[1]:
                new_range[0] = range2[1] + 1
            elif range2[1] >= new_range[1] and new_range[0] <= range2[0] <= new_range[1]:
                new_range[1] = range2[0] - 1
        return new_range
    
    def range_size(range: tuple[int, int]) -> int:
        if range is None: return 0
        return max(range[1] - range[0] + 1, 0)

    for i in range(len(ranges)):
        ranges[i] = fix_overlap(ranges[i])

    return sum(map(range_size, ranges))


def load_input(test: bool = False) -> str:
    with open(f'{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    data = load_input(TEST)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()