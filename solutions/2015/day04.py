from hashlib import md5
from itertools import count

TEST = True

def solution(data: str, zeros: int) -> int:
    for i in count(1):
        hs = md5(f"{data}{i}".encode()).hexdigest()
        if hs[0:zeros] == "0" * zeros:
            return i

def part1(data: str) -> str:
    return solution(data, 5)

def part2(data: str) -> str:
    return solution(data, 6)


def load_input(test: bool = False) -> str:
    with open(f'inputs/2015/day04_{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    data = load_input(TEST)
    print(md5(b"abcdef609043").hexdigest())
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
