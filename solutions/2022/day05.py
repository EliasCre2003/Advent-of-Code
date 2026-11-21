from dataclasses import dataclass
import re


TEST = False


@dataclass
class Instruction:
    count: int
    source: int
    destination: int


def part1(data: str) -> str:
    stacks, instructions = parse_data(data)
    for instruction in instructions:
        source = stacks[instruction.source-1]
        dest = stacks[instruction.destination-1]
        for _ in range(instruction.count):
            box = source.pop()
            dest.append(box)
    return ''.join([s[-1] for s in stacks])


def part2(data: str) -> str:
    stacks, instructions = parse_data(data)
    for instruction in instructions:
        source = stacks[instruction.source-1]
        dest = stacks[instruction.destination-1]
        stacks[instruction.source-1], moved_boxes = source[:-instruction.count], source[-instruction.count:]
        dest.extend(moved_boxes)
    return ''.join([s[-1] for s in stacks])


def parse_data(data: str) -> tuple[list[list[str]], list[Instruction]]:
    stack_str, inst_str = data.split('\n\n', maxsplit=1)
    stack_str = stack_str.splitlines()

    stacks: list[list[str]] = []
    for col in range(1, len(stack_str[-1]) + 1, 4):
        stack: list[str] = []
        for row in reversed(range(len(stack_str)-1)):
            box = stack_str[row][col]
            if box == ' ': break
            stack.append(box)
        stacks.append(stack)

    def parse_instruction(line: str) -> Instruction:
        pattern = r'move (\d+) from (\d+) to (\d+)'
        m = re.search(pattern, line)
        if not m: raise ValueError(f"Could not parse: {line}")
        return Instruction(
            int(m.group(1)),
            int(m.group(2)),
            int(m.group(3))
        )

    return stacks, list(map(parse_instruction, inst_str.splitlines()))



def load_input(test: bool = False) -> str:
    with open(f'{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    data = load_input(TEST)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()