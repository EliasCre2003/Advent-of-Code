class Rotations:
    def __init__(self, string: str):
        string = string.strip()
        self.dir = string[0]
        self.dist = int(string[1:])

def part1(rotations: list[Rotations]):
    dial = 50
    counter = 0
    for rotation in rotations:
        if rotation.dir == 'R':
            dial += rotation.dist
        elif rotation.dir == 'L':
            dial -= rotation.dist
        else:
            print("Error")
            exit()
        dial %= 100
        if dial == 0:
            counter += 1
    return counter
    

def part2(rotations: list[Rotations]):
    # dial = prev = 50
    # counter = 0
    # for rotation in rotations:
    #     if rotation.dir == 'R':
    #         dist_to_0 = 100 - dial
    #         dial += rotation.dist
    #     else:
    #         dist_to_0 = dial
    #         dial -= rotation.dist
    #     dial %= 100

    #     if prev - dist_to_0 <= 0:
    #         counter += 1
    #         distance = rotation.dist

    #     if rotation.dir == 'R' and dial < prev:
    #         counter += 1
    #     if rotation.dir == 'L' and dial > prev:
    #         counter += 1

    #     dial = prev
    # return counter

    dial = 50
    counter = 0
    for rotation in rotations:
        for _ in range(rotation.dist):
            if rotation.dir == 'R':
                dial += 1
            else:
                dial -= 1
            dial %= 100
            if dial == 0:
                counter += 1
    return counter


def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    rotations = [Rotations(line) for line in lines]

    print(part1(rotations))
    print(part2(rotations))

    
    
if __name__ == '__main__':
    main()