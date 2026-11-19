


def part1(games: list[tuple[str, str]]):
    points_map = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    win_map = {
        'X': 'C',
        'Y': 'A',
        'Z': 'B'
    }
    conversion_map = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }

    def calculate_points(game: tuple[str, str]) -> float:
        shape_points = points_map[game[1]]
        if conversion_map[game[0]] == game[1]: return shape_points + 3
        return shape_points + 6 * (game[0] == win_map[game[1]])
    
    return sum(map(calculate_points, games))


def part2(games: list[tuple[str, str]]):
    win_map = {
        'C': 'X',
        'A': 'Y',
        'B': 'Z'
    }
    tie_map = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }
    loose_map = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    }

    def calculate_shape(game: tuple[str, str]):
        match game[1]:
            case 'X': return loose_map[game[0]]
            case 'Y': return tie_map[game[0]]
            case 'Z': return win_map[game[0]]

    return part1([(game[0], calculate_shape(game)) for game in games])


def main():
    with open("input.txt", 'r') as f:
        data = f.read().strip()

    lines = data.split('\n')
    games = [game.split(' ') for game in lines]
    print(part1(games))
    print(part2(games))

main()