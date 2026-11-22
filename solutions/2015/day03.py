
TEST = True


def new_location(location: tuple[int, int], direction: str) -> tuple[int, int]:
    match direction:
        case '>': return location[0] + 1, location[1]
        case 'v': return location[0], location[1] + 1
        case '<': return location[0] - 1, location[1]
        case '^': return location[0], location[1] - 1


def part1(data: str) -> str:
    current_location = (0, 0)
    locations = {current_location}
    for direction in data:
        current_location = new_location(current_location, direction)
        locations.add(current_location)
    return len(locations)


def part2(data: str) -> str:
    santa = robot = (0, 0)
    locations = {santa}
    for i in range(0, len(data), 2):
        santa = new_location(santa, data[i])
        robot = new_location(robot, data[i+1])
        locations.add(santa)
        locations.add(robot)
    return len(locations)


def load_input(test: bool = False) -> str:
    with open(f'inputs/2015/day03_{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    data = load_input(TEST)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
