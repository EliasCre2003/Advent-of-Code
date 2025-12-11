URL = None
TEST = False

from time import time_ns

def parse_data(data: str) -> dict[str, set[str]]:
    graph: dict[str, set[str]] = {}
    for line in data.splitlines():
        key, set_str = line.split(':')
        graph[key] = set(set_str.strip().split(' '))
    return graph
    

def part1(data: str) -> str:
    graph = parse_data(data)
    cache: dict[str, int] = {}
    
    def paths(device: str) -> int:
        if device == 'out':
            return 1
        # if device in cache:
        #     return cache[device]
        cache[device] = sum(map(paths, graph[device]))
        return cache[device]

    return paths('you')


def part2(data: str) -> str:
    ...


def load_input(test: bool = False) -> str:
    with open(f'{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    data = load_input(TEST)
    start = time_ns()
    print(f'Part 1: {part1(data)}')
    end = time_ns()
    print()
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()