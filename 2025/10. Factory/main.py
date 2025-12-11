from collections import deque

TEST = False


class Button:
    def __init__(self, lights: list[int]):
        self.lights = lights
        

class MachineState:
    def __init__(self, state: list[bool], costs: list[int]):
        self.state = state
        self.costs = costs

    def new_state(self, button: list[int]) -> 'MachineState':
        new_state = self.state.copy()
        cost = 0
        for index in button:
            new_state[index] = not new_state[index]
            
            # lösning 1
            cost += self.costs[index]
            
            # lösning 2
            # if new_state[index]:
            #     cost += self.costs[index]
        
        # lösning 3
        # for i, light in enumerate(self.state):
        #     if light: cost += self.costs[i]

        return MachineState(new_state, self.costs), cost

    @staticmethod
    def new_machine(size: int, costs: list[int]) -> 'MachineState':
        return MachineState([False] * size, costs)
    
    def __str__(self):
        return f'[{''.join('#' if light else '.' for light in self.state)}]'
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other: 'MachineState'):
        if not isinstance(other, MachineState):
            return False
        return self.state == other.state and self.costs == other.costs

    def __hash__(self) -> int:
        return hash((tuple(self.state), tuple(self.costs)))


def parse_data(data: str) -> list[tuple[MachineState, list[list[int]]]]:
    lines = data.splitlines()

    def parse_line(line: str) -> tuple[MachineState, list[list[int]]]:
        req_str, but_str = line.split(' ', maxsplit=1)

        req_list = [
            c == '#'
            for c in req_str[1:-1]
        ]

        but_str_split = but_str.split(' ')

        buttons = [
            list(map(int, button[1:-1].split(',')))
            for button in but_str_split[:-1]
        ]

        joltage_req = list(map(int, but_str_split[-1][1:-1].split(',')))

        requirement = MachineState(req_list, joltage_req)

        return requirement, buttons
    
    return list(map(parse_line, lines))


def part1(data: str) -> str:
    def eval_instruction(instruction: tuple[MachineState, list[list[int]]]) -> int:
        requirement, buttons = instruction
        machine = MachineState.new_machine(len(requirement.state), requirement.costs)
        visited_dict: dict[MachineState, set[tuple]] = {}
        queue = deque([(machine, 0)])
        
        while queue:    
            current_state, current_depth = queue.popleft()
            for button in buttons:
                next_state, _ = current_state.new_state(button)
        
                if next_state == requirement:
                    return current_depth + 1
         
                if next_state not in visited_dict:
                    visited_dict[next_state] = {tuple(button)}
                else:
                    if tuple(button) in visited_dict[next_state]: continue
                    visited_dict[next_state].add(tuple(button))
         
                queue.append((next_state, current_depth + 1))
    
    instructions = parse_data(data)
    return sum(map(eval_instruction, instructions))

    


def part2(data: str) -> str:
    def eval_instruction(instruction: tuple[MachineState, list[list[int]]]) -> int:
        requirement, buttons = instruction
        machine = MachineState.new_machine(len(requirement.state), requirement.costs)
        
        visited_set = {machine}
        queue = deque([(machine, 0)])

        min_cost = 2**30
        while queue:
            current_state, current_cost = queue.popleft()
            for button in buttons:
                next_state, cost = current_state.new_state(button)
                next_cost = current_cost + cost
                if next_state == requirement:
                    if next_cost < min_cost: min_cost = next_cost
                    continue
                if next_state in visited_set:
                    continue
                visited_set.add(next_state)
                queue.append((next_state, next_cost))
        return min_cost
    
    instructions = parse_data(data)
    return sum(map(eval_instruction, instructions))


def load_input(test: bool = False) -> str:
    with open(f'{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    data = load_input(TEST)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()