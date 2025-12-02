def part1(ranges: list[tuple[str, str]]):
    total = 0
    for r in ranges:
        for i in range(int(r[0]), int(r[1]) + 1):
            num_len = len(num := str(i))
            if num_len % 2 != 0:
                continue
            div = num_len // 2
            match_num = num[0:div] * 2
            if match_num != num: continue
            total += i
    return total


def part2(ranges: list[tuple[str, str]]):
    total = 0
    for r in ranges:
        for i in range(int(r[0]), int(r[1]) + 1):
            num_len = len(num := str(i))
            for seq_len in range(1, num_len // 2 + 1):
                if num_len % seq_len != 0:
                    continue
                repeats = num_len // seq_len
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