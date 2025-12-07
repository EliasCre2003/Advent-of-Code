TEST = False



def part1(data: str) -> str:
    lines = data.splitlines()
    cache: set[tuple[int, int]] = set()
    
    def splits(x: int, y: int):
        for i in range(y, len(lines)):
            key = i, x
            if key in cache: break
            if lines[i][x] == '^':
                return splits(x-1, i) + splits(x+1, i) + 1
            cache.add(key)
        return 0
    
    return splits(lines[0].index('S'), 1)


def part2(data: str) -> str:
    lines = data.splitlines()
    cache: dict[tuple[int, int], int] = {}
    
    def timelines(x: int, y: int) -> int:
        key = x,y
        if key in cache:
            return cache[key]
        for i in range(y, len(lines)):
            if lines[i][x] != '^': continue
            cache[key] = timelines(x-1, i) + timelines(x+1, i)
            return cache[key]
        cache[key] = 1
        return 1
    
    return timelines(lines[0].index('S'), 1)


def load_input(test: bool = False) -> str:
    with open(f'{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    data = load_input(TEST)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()