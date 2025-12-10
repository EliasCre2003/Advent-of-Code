from collections import deque

TEST = False


class MachineState:
    def __init__(self, state: list[bool]):
        self.state = state

    def new_state(self, button: list[int]) -> 'MachineState':
        new_state = self.state.copy()
        for index in button:
            new_state[index] = not new_state[index]
        return MachineState(new_state)

    @staticmethod
    def new_machine(size: int) -> 'MachineState':
        return MachineState([False] * size)
    
    def __str__(self):
        return f'[{''.join('#' if light else '.' for light in self.state)}]'
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other: 'MachineState'):
        if not isinstance(other, MachineState):
            return False
        return self.state == other.state

    def __hash__(self) -> int:
        return hash(tuple(self.state))


def parse_data(data: str) -> list[tuple[MachineState, list[list[int]], list[int]]]:
    lines = data.splitlines()

    def parse_line(line: str) -> tuple[MachineState, list[list[int]], list[int]]:
        req_str, but_str = line.split(' ', maxsplit=1)

        requirement = MachineState([
            c == '#'
            for c in req_str[1:-1]
        ])

        but_str_split = but_str.split(' ')

        buttons = [
            list(map(int, button[1:-1].split(',')))
            for button in but_str_split[:-1]
        ]

        joltage_req = list(map(int, but_str_split[-1][1:-1].split(',')))

        return requirement, buttons, joltage_req
    
    return list(map(parse_line, lines))


def part1(data: str) -> str:

    def eval_instruction(instruction: tuple[MachineState, list[list[int]], list[int]]) -> int:
        requirement, buttons, _ = instruction
        machine = MachineState.new_machine(len(requirement.state))
        
        visited_set = {machine}
        queue = deque([(machine, 0)])
        while queue:
            current_state, current_depth = queue.popleft()
            for button in buttons:
                next_state = current_state.new_state(button)
                if next_state == requirement:
                    return current_depth + 1
                if next_state in visited_set:
                    continue
                visited_set.add(next_state)
                queue.append((next_state, current_depth + 1))
        return None
    
    instructions = parse_data(data)
    return sum(map(eval_instruction, instructions))


def part2(data: str) -> str:
    ...


def load_input(test: bool = False) -> str:
    with open(f'{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    data = load_input(TEST)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()