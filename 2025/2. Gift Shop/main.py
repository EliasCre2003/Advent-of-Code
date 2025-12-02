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
            match_num = num[0:div] * int(repeats)
            if match_num != num: continue
            print(i)
            total += i
    return total
    

def main():
    with open("input.txt", 'r') as f:
        line = f.read().strip()
    
    ranges_str = line.split(',')
    ranges = [range.split('-') for range in ranges_str]
    part1(ranges)


    
main()