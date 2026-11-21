import pygame as pg
import sys
from copy import copy


class Tile:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: 'Tile'):
        if not isinstance(other, Tile):
            raise ValueError('Must add with another tile')
        return Tile(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Tile'):
        if not isinstance(other, Tile):
            raise ValueError('Must sub with another tile')
        return Tile(self.x - other.x, self.y - other.y)

    def __mul__(self, scale: int):
        if not isinstance(scale, int):
            raise ValueError('Must scale with a scalar number')
        return Tile(self.x * scale, self.y * scale)
    
    def __eq__(self, other: 'Tile'):
        if not isinstance(other, Tile):
            return False
        return self.x == other.x and self.y == other.y


class Line:
    
    def __init__(self, tile1: Tile, tile2: Tile):
        self.horizontal = tile1.y == tile2.y
        if not (tile1.x == tile2.x or self.horizontal):
            raise ValueError('Line must "straight"')
        # if tile1.x == tile2.x and self.horizontal:
        #     raise ValueError('Line cant have a length == 1')
        self.tile1 = tile1
        self.tile2 = tile2
    
    
    def size(self) -> int:
        if self.horizontal:
            return abs(self.tile1.x - self.tile2.x) + 1
        else:
            return abs(self.tile1.y - self.tile2.y) + 1
    
    def is_positive(self):
        if self.horizontal:
            return self.tile1.x > self.tile2.x
        else:
            return self.tile1.y > self.tile2.y
        
    def __copy__(self):
        return Line(copy(self.tile1), copy(self.tile2))
        
    
    @staticmethod
    def intersect(line1: 'Line', line2: 'Line') -> bool:
        if line1.horizontal or not line2.horizontal:
            return ValueError("Line 1 must be vertical and line 2 must be horizontal")

        line2 = copy(line2)
        if line2.is_positive():
            line2.tile1.x += 1
            line2.tile2.x -= 1
        else:
            line2.tile1.x -= 1
            line2.tile2.x += 1
        
        if (line1.tile1.x > line2.tile1.x and line1.tile1.x > line2.tile2.x or
            line1.tile1.x < line2.tile1.x and line1.tile1.x < line2.tile2.x):
            return False
        
        if not line1.is_positive():
            line1 = Line(line1.tile2, line1.tile1)
        
        if line1.tile1.y < line2.tile1.y and line1.tile2.y > line2.tile1.y:
            return True

        return False
    


def get_red_tiles(data: str) -> list[tuple[int, int]]:
    return [
        tuple(map(int, box)) for box in
        map(lambda x: x.split(','), data.splitlines())
    ]

# def draw():


def four_occurences(tiles):
    x_occ = {}
    y_occ = {}

    for tile in tiles:
        if tile[0] not in x_occ:
            x_occ[tile[0]] = 1
        else:
            x_occ[tile[0]] += 1
        
        if tile[1] not in y_occ:
            y_occ[tile[1]] = 1
        else:
            y_occ[tile[1]] += 1
    

    for key in x_occ.keys():
        if x_occ[key] == 3:
            print(key)


def rect_size(tile1: Tile, tile2: Tile) -> int:
    dx = abs(tile1.x - tile2.x) + 1
    dy = abs(tile1.y - tile2.y) + 1
    return dx * dy


def part2(data: str):
    red_tiles = [
        Tile(*map(int, box)) for box in
        map(lambda x: x.split(','), data.splitlines())
    ]

    cheat_tiles = [
        Tile(94710, 50238),
        Tile(94710, 48527)
    ]

    collision_lines: list[Line] = []
    prev_tile = red_tiles[0]
    for tile in red_tiles[1:]:
        line = Line(prev_tile, tile)
        if line.horizontal:
            collision_lines.append(line)
        prev_tile = tile
    line = Line(red_tiles[-1], red_tiles[0])
    if line.horizontal:
        collision_lines.append(line)

    # for t in cheat_tiles:
    #     red_tiles.remove(t)

    max_size = 0
    max_rect = None
    for i, cheat_tile in enumerate(cheat_tiles):
        for r_tile in red_tiles:
            if i == 0 and r_tile.y < cheat_tile.y:
                continue
            elif i == 1 and r_tile.y > cheat_tile.y:
                continue
            if r_tile.y > 68128 or r_tile.y < 34256:
                continue
            size = rect_size(cheat_tile, r_tile)
            if size <= max_size:
                continue
            check_lines = [
                Line(
                    cheat_tile,
                    Tile(cheat_tile.x, r_tile.y)
                ),
                Line(
                    r_tile,
                    Tile(r_tile.x, cheat_tile.y)
                )
            ]
            bad = False
            for line1 in check_lines:
                for line2 in collision_lines:
                    if Line.intersect(line1, line2):
                        bad = True
                        break
                if bad:
                    break
            else:
                max_size = size
                max_rect = cheat_tile, r_tile
    print(max_size)
    return max_rect




def main():
    with open('input.txt', 'r') as f:
        data = f.read().rstrip()

    corners = part2(data)
    corners = [
        corners[0],
        Tile(corners[0].x, corners[1].y),
        corners[1],
        Tile(corners[1].x, corners[0].y)
    ]
    

    red_tiles = get_red_tiles(data)

    # four_occurences(red_tiles)

    min_x = min(tile[0] for tile in red_tiles)
    max_x = max(tile[0] for tile in red_tiles)

    min_y = min(tile[1] for tile in red_tiles)
    max_y = max(tile[1] for tile in red_tiles)

    pg.init()

    SIZE = WIDTH, HEIGHT = 1000, 1000
    screen = pg.display.set_mode(SIZE)

    x_scale = WIDTH / (max_x - min_x)
    y_scale = HEIGHT / (max_y - min_y)

    polygon_points = [
        ((tile[0] - min_x) * x_scale,
         (tile[1] - min_y) * y_scale)
        for tile in red_tiles
    ]

    rect_points = [
        ((tile.x - min_x) * x_scale, (tile.y - min_y) * y_scale)
        for tile in corners
    ]



    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.image.save(screen, 'solution_part2.png')
                pg.quit()
                sys.exit()
        mouse = pg.mouse.get_pos()
        # print(mouse[0] / x_scale + min_x, mouse[1] / y_scale + min_y)
        screen.fill((0,0,0))
        pg.draw.polygon(screen, (255, 255, 255), polygon_points)
        pg.draw.polygon(screen, (255, 0, 0), rect_points)
        pg.display.flip()

main()

# t1 = Tile(1, 2)
# t2 = Tile(1, 6)
# l1 = Line(t1, t2)

# l2 = copy(l1)

# l2.tile1.x += 1

# print(l1)