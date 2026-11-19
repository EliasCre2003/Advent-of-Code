def part1(elf_strings: list[str]):
    return max(sum(int(c) for c in string.split('\n')) for string in elf_strings)

def part2(elf_strings: list[str]):
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
    
    elf_strings = data.split('\n\n')
    print(part1(elf_strings))
    print(part2(elf_strings))


if __name__ == '__main__':
    main()