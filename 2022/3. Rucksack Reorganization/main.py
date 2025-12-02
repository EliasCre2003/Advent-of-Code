TEST = False


class Rucksack:
    def __init__(self, string: str):
        half_str_len = len(string) // 2
        self.comp1 = string[:half_str_len]
        self.comp2 = string[half_str_len:]


def load_input(test: bool = False) -> str:
    with open(f'{"test" if test else "input"}.txt', 'r') as f:
        return f.read().strip()


def priority(c: str) -> int:
    if c.isupper():
        return ord(c) - 38
    else:
        return ord(c) - 96

def split_content(rucksack: str) -> tuple[str, str]:
    half_str_len = len(rucksack) // 2
    comp1 = rucksack[:half_str_len]
    comp2 = rucksack[half_str_len:]
    return comp1, comp2

def part1(rucksacks: list[str]) -> str:
    def sum_priorities(rucksack: str) -> int:
        comp1, comp2 = split_content(rucksack)
        intersection = set(comp1).intersection(set(comp2))
        return sum(map(priority, intersection))
    
    return sum(sum_priorities(rucksack) for rucksack in rucksacks)


def part2(rucksacks: list[Rucksack]) -> str:
    rucksacks = rucksacks.copy()
    badges = []
    while rucksacks:
        commons = set(rucksacks.pop(0))
        for _ in range(2):
            commons = commons.intersection(set(rucksacks.pop(0)))
        badges.append(list(commons)[0])
    return sum(map(priority, badges))
        
        # groups.append(group)
        
    
    # for group in groups:



def main():
    data = load_input(TEST)
    lines = data.split('\n')
    # rucksacks = [Rucksack(line) for line in lines]
    print(part1(lines))
    print(part2(lines))

if __name__ == '__main__':
    main()