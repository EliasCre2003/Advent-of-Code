TEST = False

def load_input(test: bool = False) -> str:
    with open(f'{"test" if test else "input"}.txt', 'r') as f:
        return f.read().strip()


def part1(banks: list[list[int]]) -> str:
    def find_best(bank: list[int]) -> int:
        bank = bank.copy()
        b_temp = max(bank)
        if bank.index(b_temp) == len(bank) - 1:
            b2 = bank.pop()
            b1 = max(bank)
        else:
            b1 = b_temp
            ind = bank.index(b1)
            b2 = max(bank[ind+1:])
        return int(str(b1) + str(b2))
    return sum(map(find_best, banks))



def part2(banks: list[list[int]]) -> str:
    def find_best(bank: list[int]) -> int:
        flexibility = len(bank) - 12
        number = []
        bank = bank.copy()
        while flexibility > 0 and len(bank) > flexibility:
            max_num = -1
            max_ind = -1
            for j in range(min(flexibility+1, len(bank))):
                if bank[j] > max_num: 
                    max_num = bank[j]
                    max_ind = j
            flexibility -= max_ind
            bank = bank[max_ind+1:]
            number.append(max_num)
        while len(number) < 12:
            number.append(bank.pop(0))
        return int(''.join(map(str, number)))

    return sum(map(find_best, banks))


def main():
    data = load_input(TEST)
    lines = data.split('\n')
    banks = [[int(b) for b in line] for line in lines]
    print(f'Part 1: {part1(banks)}')
    print(f'Part 2: {part2(banks)}')



if __name__ == '__main__':
    main()