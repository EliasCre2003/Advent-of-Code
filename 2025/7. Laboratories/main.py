TEST = False



def part1(data: str) -> str:
    lines = list(map(list, data.splitlines()))
    
    def dfs(x, y):
        for i in range(y, len(lines)):
            cell = lines[i][x]
            if cell == '|':
                break
            if cell == '^':
                return dfs(x-1, i) + dfs(x+1, i) + 1
            lines[i][x] = '|'
        return 0
    
    return dfs(lines[0].index('S'), 1)


def part2(data: str) -> str:
    lines = list(map(list, data.splitlines()))
    cache: dict[tuple[int, int], int] = {}
    
    def dfs(x: int, y: int) -> int:
        key = x,y
        if key in cache:
            return cache[key]
        for i in range(y, len(lines)):
            if lines[i][x] != '^': continue
            cache[key] = dfs(x-1, i) + dfs(x+1, i)
            return cache[key]
        cache[key] = 1
        return 1
    
    return dfs(lines[0].index('S'), 1)


def load_input(test: bool = False) -> str:
    with open(f'{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    data = load_input(TEST)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()