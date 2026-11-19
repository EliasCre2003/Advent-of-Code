TEST = False

def eval_equations(equations: list[int]) -> int:
    nums, op = equations
    n1 = nums[0]
    for n2 in nums[1:]:
        if op == '*': n1 *= n2
        else: n1 += n2
    return n1
    

def part1(data: str) -> str:
    lines = data.splitlines()
    op_str = lines.pop()

    def parse_num_line(line: str):
        return list([int(num) 
                     for num in line.split(' ') 
                     if num.isnumeric()])

    num_lines = list(map(parse_num_line, lines))
    ops = list([op for op in op_str.split(' ') if op in '*+' and op != ''])
    num_cols = [([
        num_lines[j][i]
        for j in range(len(num_lines))
    ], ops[i]) for i in range(len(num_lines[0]))]
    
    return sum(map(eval_equations, num_cols))


def part2(data: str) -> str:
    lines = data.splitlines()
    
    equations = []
    for i, op in enumerate(lines[-1]):
        if op not in '*+': continue
        equation = []
        for j in range(i, len(lines[-1])):
            num = ''
            for k in range(len(lines)-1):
                digit = lines[k][j]
                num += digit
            num = num.rstrip().lstrip()
            if not num.isnumeric(): break
            equation.append(int(num))
        equations.append((equation, op))
    
    return sum(map(eval_equations, equations))


def load_input(test: bool = False) -> str:
    with open(f'{"test" if test else "input"}.txt', 'r') as f:
        return f.read()


def main():
    data = load_input(TEST)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()