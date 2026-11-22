TEST = True


def part1(data: str) -> str:

    vowels = 'aeiou'
    forbidden = ['ab', 'cd', 'pq', 'xy']
    
    def is_nice(string: str) -> bool:
        if len(list(filter(lambda c: c in vowels, string))) < 3:
            return False
        for s in forbidden:
            if s in string: return False   
        for i, c in enumerate(string[:-1]):
            if c == string[i+1]: return True
        return False
    
    lines = data.splitlines()
    return len(list(filter(is_nice, lines)))


def part2(data: str) -> str:

    def is_nice(string: str) -> bool:
        prop1 = prop2 = False
        for i, char in enumerate(string[:-2]):
            pair = char + string[i+1]
            if (not prop1) and (pair in string[i+2:]):
                prop1 = True
            if (not prop2) and (char == string[i+2]):
                prop2 = True
            if prop1 and prop2: 
                return True
        return False
        
    lines = data.splitlines()
    return len(list(filter(is_nice, lines)))


def load_input(test: bool = False) -> str:
    with open(f'inputs/2015/day05_{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    data = load_input(TEST)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    # main()
    print('ab' in 'acb')