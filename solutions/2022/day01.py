def part1(data: str):
    elf_strings = data.split('\n\n')
    return max(sum(int(c) for c in string.split('\n')) for string in elf_strings)

def part2(data: str):
    elf_strings = data.split('\n\n')
    calories = [sum(int(c) for c in string.split('\n')) for string in elf_strings]
    total = 0
    for _ in range(3):
        max_c = max(calories)
        calories.remove(max_c)
        total += max_c
    return total

def main():
    with open("input.txt", 'r') as f:
        data = f.read().strip()
    
    print(part1(data))
    print(part2(data))


if __name__ == '__main__':
    main()