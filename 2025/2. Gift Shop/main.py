from math import sqrt, ceil

def part1(ranges: list[tuple[int, int]]):
    
    total = 0
    for r in ranges:
        for i in range(int(r[0]), int(r[1]) + 1):
            num_len = len(num := str(i))
            repeats = 2
            if num_len % 2 != 0:
                continue
            div = num_len // repeats
            match_num = num[0:div] * repeats
            if match_num != num: continue
            print(i)
            total += i
    return total


def part2(ranges: list[tuple[int, int]]):
    total = 0
    for r in ranges:
        for i in range(int(r[0]), int(r[1]) + 1):
            num_len = len(num := str(i))
            for seq_len in range(1, num_len // 2 + 1):
                repeats = num_len / seq_len
                if not repeats.is_integer():
                    continue
                repeats = int(repeats)
                match_num = num[0:seq_len] * repeats
                if match_num != num: continue
                total += i
                break
    return total


def main():
    with open("input.txt", 'r') as f:
        line = f.read().strip()
    ranges_str = line.split(',')
    ranges = [range.split('-') for range in ranges_str]

    print(f"Part 1: {part1(ranges)}")
    print(f"Part 2: {part2(ranges)}")


if __name__ == "__main__":
    main()