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