TEST = True


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

    def fix_overlap(r1: tuple[int, int]) -> tuple[int, int]:
        new_r = list(r1)
        for r2 in ranges:
            if r2 is None: continue
            if r2 == r1: continue
            if r2[0] <= new_r[0] and r2[1] >= new_r[1]:
                return None
            if r2[0] <= new_r[0] and new_r[0] <= r2[1] <= new_r[1]:
                new_r[0] = r2[1] + 1
            elif r2[1] >= new_r[1] and new_r[0] <= r2[0] <= new_r[1]:
                new_r[1] = r2[0] - 1
        return new_r
    
    def range_size(r: tuple[int, int]) -> int:
        if r is None: return 0
        return max(r[1] - r[0] + 1, 0)

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