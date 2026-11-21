TEST = False


def load_input(test: bool = False) -> str:
    with open(f'{"test" if test else "input"}.txt', 'r') as f:
        return f.read().strip()


def find_best(bank: list[int], n: int) -> int:
    flexibility = len(bank) - n
    number = []
    bank = bank.copy()
    while flexibility > 0 and len(bank) > flexibility:
        max_num = max_ind = -1
        for i in range(min(flexibility+1, len(bank))):
            if bank[i] <= max_num: continue
            max_num = bank[i]
            max_ind = i
        flexibility -= max_ind
        bank = bank[max_ind+1:]
        number.append(max_num)
    number.extend(bank)
    return int(''.join(map(str, number[:n])))


def part1(banks: list[list[int]]) -> str:
    return sum(map(lambda b: find_best(b, 2), banks))


def part2(banks: list[list[int]]) -> str:
    return sum(map(lambda b: find_best(b, 12), banks))


def main():
    data = load_input(TEST)
    lines = data.split('\n')
    banks = [[int(b) for b in line] for line in lines]
    print(f'Part 1: {part1(banks)}')
    print(f'Part 2: {part2(banks)}')


if __name__ == '__main__':
    main()