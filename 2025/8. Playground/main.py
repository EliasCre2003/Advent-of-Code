TEST = True

from math import prod

class Connection:
    def __init__(self, box1: 'Box', box2: 'Box', distance: float):
        self.box1 = box1
        self.box2 = box2
        self.distance = distance
    
    def __lt__(self, other: 'Connection') -> bool:
        return self.distance < other.distance

class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def connection(self, box: 'Box') -> Connection:
        dist = ((self.x - box.x) ** 2 + (self.y - box.y) ** 2 + (self.z - box.z) ** 2) ** (1 / 2)
        return Connection(self, box, dist) 


def generate_graph(boxes: Box, top_shortest: int) -> dict[Box, set[Box]]:
    connections: list[Connection] = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            connections.append(boxes[i].connection(boxes[j]))
    connections.sort()
    shortest_connections = connections[:top_shortest]
    connection_map: dict[Box, set[Box]] = {
        box: set()
        for box in boxes
    }
    for conn in shortest_connections:
        connection_map[conn.box1].add(conn.box2)
        connection_map[conn.box2].add(conn.box1)
    return connection_map


def part1(data: str) -> str:
    boxes = [
        Box(*map(int, box)) for box in
        map(lambda x: x.split(','), data.splitlines())
    ]
    box_graph = generate_graph(boxes, 1000 - 990 * TEST)

    visited: set[Box] = set()
    circuits: list[list[Box]] = []
    def find_circuit(box: Box) -> list[Box]:
        visited.add(box)
        network = [box]
        for connected in box_graph[box]:
            if connected not in visited: 
                network += find_circuit(connected)
        return network
    for box in box_graph:
        if box in visited: continue
        circuits.append(find_circuit(box))
    
    circuits.sort(key=lambda x: len(x))
    circuits = list(reversed(circuits))[:3]

    return prod(map(len, circuits))


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