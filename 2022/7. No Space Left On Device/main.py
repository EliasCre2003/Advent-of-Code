URL = None
TEST = False


from dataclasses import dataclass


@dataclass
class File:
    size: int
    name: str

    def __hash__(self):
        return hash((self.size, self.name))


def build_file_system(data: str) -> dict[str, set[File | str]]:
    file_system: dict[str, set[File | str]] = {}
    current_dir = ''
    for line in data.splitlines():
        line = line.strip()
        if line.startswith('$ '):
            if not line.removeprefix('$ ').startswith('cd'): continue
            line = line.removeprefix('$ cd ')
            if line == '/':
                current_dir = '/'
            elif line == '..':
                current_dir = current_dir[:-1].rsplit('/', maxsplit=1)[0] + '/'
            else:
                current_dir += line + '/'
        else:
            if not current_dir in file_system:
                file_system[current_dir] = set()
            arg1, arg2 = line.split(' ')
            if arg1 == 'dir':
                file_system[current_dir].add(f'{current_dir}{arg2}/')
            else:
                file_system[current_dir].add(File(int(arg1), arg2))
    return file_system


def directory_size(directory: str, file_system: dict[str, set[File | str]], cache: dict[str, int] = {}) -> int:
    if directory in cache:
        return cache[directory]
    size = 0
    for element in file_system[directory]:
        if isinstance(element, File):
            size += element.size
        else:
            size += directory_size(element, file_system, cache)
    cache[directory] = size
    return size

def directory_sizes(file_system: dict[str, set[File | str]]) -> dict[str, int]:
    cache: dict[str, int] = {}
    directory_size('/', file_system, cache)
    return cache


def part1(sizes: dict[str, int]) -> str:
    return sum([
        size for size in sizes.values()
        if size < 100_000
    ])



def part2(sizes: dict[str, int]) -> str:
    space_to_remove = sizes['/'] - 40_000_000
    return min([
        size for size in sizes.values()
        if size >= space_to_remove
    ])



def load_input(test: bool = False) -> str:
    with open(f'{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    data = load_input(TEST)
    file_system = build_file_system(data)
    sizes = directory_sizes(file_system)
    print(f'Part 1: {part1(sizes)}')
    print(f'Part 2: {part2(sizes)}')


if __name__ == '__main__':
    main()