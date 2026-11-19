TEST = False


def roll_is_accessible(x: int, y: int, data: list[list[str]]) -> bool:
        if data[y][x] != '@': return False
        total = 0
        for x_off in range(-1, 2):
            for y_off in range(-1, 2):
                if x_off == y_off == 0: continue
                x_ind, y_ind = x + x_off, y + y_off
                if not (x_ind < 0 or y_ind < 0 or x_ind >= len(data[0]) or y_ind >= len(data)):
                    total += data[y_ind][x_ind] == '@'
                if total >= 4: return False
        return True


def parse_data(data: str) -> list[list[str]]:
    return list(map(list, data.splitlines()))


def part1(data: str) -> str:
    data = parse_data(data)
    total = 0
    
    for y in range(len(data)):
        row_tot = 0
        for x in range(len(data[0])):
            row_tot += roll_is_accessible(x, y, data)
        total += row_tot
    return total

        
def part2(data: str) -> str:
    data = parse_data(data)
    
    total = 0
    while True:
        removed = []
        for y in range(len(data)):
            for x in range(len(data[0])):
                if not roll_is_accessible(x, y, data): continue
                removed.append((x, y))
                total += 1
        if len(removed) == 0:
            break
        for x, y in removed:
            data[y][x] = 'x'
        removed = []
    return total


def load_input(test: bool = False) -> str:
    with open(f'{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    data = load_input(TEST)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()