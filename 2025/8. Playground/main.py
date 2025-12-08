TEST = False

from math import prod
from dataclasses import dataclass

class Connection:
    def __init__(self, box1: 'Box', box2: 'Box'):
        self.box1 = box1
        self.box2 = box2
        self.distance = Box.distance(box1, box2)
    
    def __lt__(self, other: 'Connection') -> bool:
        return self.distance < other.distance


class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    @staticmethod
    def distance(box1: 'Box', box2: 'Box') -> float:
        return ((box1.x - box2.x) ** 2 + (box1.y - box2.y) ** 2 + (box1.z - box2.z) ** 2) ** (1 / 2)
    

def generate_graph(boxes: list[Box], connections: list[Connection]) -> dict[Box, set[Box]]:
    connection_map: dict[Box, set[Box]] = {
        box: set()
        for box in boxes
    }
    for conn in connections:
        connection_map[conn.box1].add(conn.box2)
        connection_map[conn.box2].add(conn.box1)
    return connection_map


def part1(boxes: list[Box], connections: list[Connection]) -> str:
    box_graph = generate_graph(boxes, connections[:(1000 - 990 * TEST)])
    visited: set[Box] = set()
    def find_circuit(box: Box) -> list[Box]:
        visited.add(box)
        network = [box]
        for connected in box_graph[box]:
            if connected not in visited: 
                network += find_circuit(connected)
        return network
    
    circuits: list[list[Box]] = []
    for box in box_graph:
        if box in visited: continue
        circuits.append(find_circuit(box))
    circuits.sort(key=lambda x: len(x))
    circuits = list(reversed(circuits))[:3]
    return prod(map(len, circuits))


def part2(boxes: list[Box], connections: list[Connection]) -> int:
    for i in range(1000 - 990 * TEST, len(connections)+1):
        top_connections = connections[:i]
        box_graph = generate_graph(boxes, top_connections)
        visited: set[Box] = set()

        def find_circuit(box: Box) -> list[Box]:
            visited.add(box)
            network = [box]
            for connected in box_graph[box]:
                if connected not in visited: 
                    network += find_circuit(connected)
            return network

        circuit = None
        for box in box_graph:
            if box in visited: continue
            if circuit: break
            circuit = find_circuit(box) 
        else: return top_connections[-1].box1.x * top_connections[-1].box2.x


def load_input(test: bool = False) -> str:
    with open(f'{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    data = load_input(TEST)
    boxes = [
        Box(*map(int, box)) for box in
        map(lambda x: x.split(','), data.splitlines())
    ]
    connections: list[Connection] = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            # connections.append(boxes[i].connection(boxes[j]))
            connections.append(Connection(boxes[i], boxes[j]))
    connections.sort()
    print(f'Part 1: {part1(boxes, connections)}')
    print(f'Part 2: {part2(boxes, connections)}')


if __name__ == '__main__':
    main()