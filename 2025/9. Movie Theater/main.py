URL = None
TEST = True


def rect_size(tile1: tuple[int, int], tile2: tuple[int, int]) -> int:
    dx = abs(tile1[0] - tile2[0]) + 1
    dy = abs(tile1[1] - tile2[1]) + 1
    return dx * dy

def opposite_tiles(tile1: tuple[int, int], tile2: tuple[int, int]) -> int:
    ot1 = tile1[0], tile2[1]
    ot2 = tile2[0], tile1[1]
    return ot1, ot2

def get_red_tiles(data: str) -> list[tuple[int, int]]:
    return [
        tuple(map(int, box)) for box in
        map(lambda x: x.split(','), data.splitlines())
    ]


def part1(data: str) -> str:
    tiles = get_red_tiles(data)
    return max(
        rect_size(tile1, tile2)
        for i, tile1 in enumerate(tiles)
        for tile2 in tiles[(i+1):]
    )

def tile_lines(red_tiles: list[tuple[int, int]]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    # prev_tile = red_tiles[0]
    # ranges = []
    # for tile in red_tiles[1:]:
    #     if tile[0] == prev_tile[0]:
    #         common = tile[0]
    #         if tile[1] > prev_tile[1]:
    #             r = range(prev_tile[1], tile[1]+1)
    #         else:
    #             r = range(prev_tile[1]+1, tile[1])
    #         ranges.append((common, r))
    #     else:
    #         common = tile[1]
    #         if tile[0] > prev_tile[0]:
    #             r = range(prev_tile[0], tile[0]+1)
    #         else:
    #             r = range(prev_tile[0]+1, tile[0])
    #         ranges.append((r, common))
    # return 
    lines = []
    prev_tile = red_tiles[0]
    for tile in red_tiles[1:]:
        lines.append((prev_tile, tile))
        prev_tile = tile
    return lines + [(red_tiles[-1], red_tiles[0])]


def cross_product(t1: tuple[int, int], t2: tuple[int, int]) -> int:
    return t1[0] * t2[1] - t1[1] * t2[0]

# def direction_vector(t1: tuple[int, int], t2: tuple[int, int]):
#     return t2[0] - t1[0], t2[1] - t1[1]

def direction_vector(t1: tuple[int, int], t2: tuple[int, int]):
    return t2[0] - t1[0], t2[1] - t1[1]

def minus(t1: tuple[int, int], t2: tuple[int, int]):
    return t1[0] - t2[0], t1[1] - t2[1]

def lines_intersect(line1: tuple[tuple[int, int], tuple[int, int]], line2: tuple[tuple[int, int], tuple[int, int]]) -> bool:
    # ax1, ay1 = line1[0]
    # ax2, ay2 = line1[1]
    # bx1, by1 = line2[0]
    # bx2, by2 = line2[1]

    # r = (ax2 - ax1, ay2 - ay1)
    # s = (bx2 - bx1, by2 - by1)

    # rxs = cross_product(r, s)
    # q_p = (bx1 - ax1, by1 - ay1)

    # if rxs != 0:
    #     # Non-parallel: use parametric form
    #     t = cross_product(q_p, s) / rxs
    #     u = cross_product(q_p, r) / rxs
    #     return 0 <= t <= 1 and 0 <= u <= 1

    # # Parallel: check if collinear
    # if cross_product(q_p, r) != 0:
    #     return False  # parallel, non-collinear

    # # Collinear: project onto dominant axis and examine 1D intervals
    # if abs(r[0]) >= abs(r[1]):
    #     # Use x-coordinates
    #     a_lo, a_hi = sorted((ax1, ax2))
    #     b_lo, b_hi = sorted((bx1, bx2))
    # else:
    #     # Use y-coordinates
    #     a_lo, a_hi = sorted((ay1, ay2))
    #     b_lo, b_hi = sorted((by1, by2))

    # overlap_start = max(a_lo, b_lo)
    # overlap_end = min(a_hi, b_hi)

    # if overlap_end < overlap_start:
    #     return 0  # no overlap

    # # Full containment? (one interval completely covers the other)
    # if (overlap_start == a_lo and overlap_end == a_hi) or \
    #    (overlap_start == b_lo and overlap_end == b_hi):
    #     return False  # your first example

    # # Partial overlap (but not full containment)
    # return True  # your second example
    (ax1, ay1), (ax2, ay2) = line1
    (bx1, by1), (bx2, by2) = line2

    r = (ax2 - ax1, ay2 - ay1)
    s = (bx2 - bx1, by2 - by1)

    rxs = cross_product(r, s)
    q_p = (bx1 - ax1, by1 - ay1)

    if rxs != 0:
        t = cross_product(q_p, s) / rxs
        u = cross_product(q_p, r) / rxs
        # strict interior only: endpoints do NOT count as intersections
        return 0 < t < 1 and 0 < u < 1

    # Parallel
    if cross_product(q_p, r) != 0:
        return False  # parallel, non-collinear

    # Collinear: for the “square inside” check, you probably
    # want to allow edges lying on the boundary, so:
    return False


def n_intersections(line: tuple[tuple[int, int], tuple[int, int]], shape: list[tuple[tuple[int, int], tuple[int, int]]]) -> int:
    return sum(
        lines_intersect(line, shape_line)
        for shape_line in shape
    )


def is_inside(tile: tuple[int, int], tile_lines: list[tuple[tuple[int, int], tuple[int, int]]]) -> bool:
    intersection_line = tile, (tile[0], tile[1] + 99999999999)
    # inter_dir_vec = direction_vector(*intersection_line)
    # intersections = sum(
    #     lines_intersect(intersection_line, line)
    #     for line in tile_lines
    # )

    return n_intersections(intersection_line, tile_lines) % 2 == 1

    # for lines in tile_lines:
    #     if is_on_line(tile, line): return True

    # for line in tile_lines:
    #     line_dir_vec = direction_vector(*line)
        
    #     # if cross-product == 0, lines are "paralel", no intersec
    #     if (cross := cross_product(inter_dir_vec, line_dir_vec)) == 0:
    #         continue
        
    #     # diff = direction_vector(line[0], intersection_line[0])
    #     diff = minus(line[0], intersection_line[0])
    #     t = cross_product(diff, line_dir_vec) / cross
    #     u = cross_product(diff, inter_dir_vec) / cross

    #     intersections += (0 <= t <= 1) and (0 <= u <= 1)
    
    # return intersections % 2 == 1


def square_lines(square: tuple[tuple[int, int], tuple[int, int]]) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    sq1, sq2 = square
    op1, op2 = opposite_tiles(*square)
    return [(sq1, op1), (op1, sq2), (sq2, op2), (op2, sq1)]


def is_on_line(tile: tuple[int, int], line: tuple[tuple[int, int], tuple[int, int]]) -> bool:
    if cross_product(direction_vector(*line), minus(tile, line[0])) != 0:
        return False

    return (min(line[0][0], line[1][0]) <= tile[0] <= max(line[0][0], line[1][0]) and
            min(line[0][1], line[1][1]) <= tile[1] <= max(line[0][1], line[1][1]))


def part2(data: str) -> str:
    red_tiles = get_red_tiles(data)
    tile_shape = tile_lines(red_tiles)
    max_size = 0
    max_tiles = None
    for i, tile1 in enumerate(red_tiles):
        for tile2 in red_tiles[(i+1):]:
            # ot = opposite_tiles(tile1, tile2)
            # # if not (ot[0] in red_tiles and ot[1] in red_tiles):
            # if not (is_inside(ot[0], tile_shape) and is_inside(ot[1], tile_shape)):
            #     continue
            bad_square = False
            square = square_lines((tile1, tile2))
            for line1 in square:
                for line2 in tile_shape:
                    if lines_intersect(line1, line2):
                        bad_square = True
                        break
                if bad_square:
                    break
            if bad_square:
                continue

            size = rect_size(tile1, tile2)
            if size > max_size: 
                max_size = size
                max_tiles = tile1, tile2
    print(max_tiles)
    return max_size



def load_input(test: bool = False) -> str:
    with open(f'{"test" if test else "input"}.txt', 'r') as f:
        return f.read().rstrip()


def main():
    data = load_input(TEST)
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == '__main__':
    main()
    # print([1,2,3,4][1:])


# ..............
# .......#...O..
# ..............
# ..O....#......
# ..............
# ..#......#....
# ..............
# .........#.#..
# ..............