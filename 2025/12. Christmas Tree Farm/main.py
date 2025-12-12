TEST = False
from math import prod


def count_presents(presents: list[str]):
    return sum(presents[j][i] == '#' for i in range(3) for j in range(3))


def load_input(test: bool = False) -> str:
    with open(f'{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def eval_line(line: str, shapes: list[int]):
    dim, set_str = line.split(':')
    size = prod(map(int, dim.split('x')))
    counts = list(map(int, set_str.strip().split(' ')))
    return size >= sum(c * shapes[i] for i, c in enumerate(counts))


def main():
    data = load_input(TEST)
    split = data.split('\n\n')
    shape_strs, region_str = split[:-1], split[-1]
    shapes = [
        count_presents(shape.splitlines()[1:])
        for shape in shape_strs
    ]
    print(sum(
        eval_line(line, shapes)
        for line in region_str.splitlines()
    ))


if __name__ == '__main__':
    main()