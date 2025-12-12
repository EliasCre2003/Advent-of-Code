TEST = False
from time import time_ns

def parse_data(data: str) -> dict[str, set[str]]:
    graph: dict[str, set[str]] = {}
    for line in data.splitlines():
        key, set_str = line.split(':')
        graph[key] = set(set_str.strip().split(' '))
    return graph


def paths(start: str, end: str, graph: dict[str, set[str]], cache: dict[str, int]) -> int:
    if start == end:
        return 1
    if start == 'out':
        return 0
    if start in cache:
        return cache[start]
    cache[start] = sum(map(lambda x: paths(x, end, graph, cache), graph[start]))
    return cache[start]


def part1() -> str:
    data = load_input(TEST, 1)
    graph = parse_data(data)
    return paths('you', 'out', graph, {})


def part2() -> str:
    data = load_input(TEST, 2)
    graph = parse_data(data)
    return (paths('svr', 'dac', graph, {}) * 
            paths('dac', 'fft', graph, {}) * 
            paths('fft', 'out', graph, {}) +
            paths('svr', 'fft', graph, {}) * 
            paths('fft', 'dac', graph, {}) * 
            paths('dac', 'out', graph, {}))


def load_input(test: bool, part: int) -> str:
    with open(f'{f"test{part}" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    start = time_ns()
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
    end = time_ns()
    print((end-start) / 1_000_000)


if __name__ == '__main__':
    main()