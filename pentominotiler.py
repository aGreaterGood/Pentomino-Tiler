# Squares defined by their centers on the grid

pentomino_l = [
    '11111',

    '1111 '+
    '0001',

    '1111 '+
    '0010',

    '1110 '+
    '0011',

    '111 '+
    '011',

    '111 '+
    '101',

    '111 '+
    '010 '+
    '010',

    '110 '+
    '010 '+
    '011',

    '111 '+
    '100 '+
    '100',

    '110 '+
    '011 '+
    '010',

    '010 '+
    '111 '+
    '010',

    '110 '+
    '011 '+
    '001'
]

pentomino_names = [
    'line', 'hook', 'nose', 'zag', 'square', 
    'cup', 'T', 'Z', 'corner', 'crane', 
    'plus', 'W'
]

pentomino_l = [[[c=='1' for c in l] for l in p.split(' ')] for p in pentomino_l]


# Rotation maintains top and left boundaries
def rotate_translate_reflect(pentomino_i, rotation, translation, reflect):
    global pentomino_l
    coord_l = []
    p = pentomino_l[pentomino_i]
    mi, mj = len(p)-1, len(p[0])-1 
    for i in range(len(p)):
        for j in range(len(p[0])):
            if p[i][j]:
                xi, xj = i, j
                if reflect: xi, xj = xi, mj-xj
                if rotation == 0: xi, xj = xi, xj       #x, y
                if rotation == 1: xi, xj = xj, mi-xi    #y, -x
                if rotation == 2: xi, xj = mi-xi, mj-xj #-x, -y
                if rotation == 3: xi, xj = mj-xj, xi    #-y, x
                coord_l.append((translation[0] + xi, translation[1] + xj))
    return sorted(coord_l)

# for i in range(4):
#     for j in range(2):
#         print(i, j)
#         print(rotate_translate_reflect(1, i, (0, 0), j))

def is_valid(shape, grid):
    def in_bounds(coord, grid):
        return 0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid[0])
    empty = -1
    return all(in_bounds((x, y), grid) and grid[x][y] == empty for x, y in shape)

check_count = 0
def tile(grid_dim, pen_i_l, grid=None):
    global check_count
    grid_x, grid_y = grid_dim
    if grid == None:
        grid = [[-1]*grid_y for i in range(grid_x)]
    check_count += 1
    # if check_count % 10**2 == 0:
    #     print(check_count)
    #     [print(l) for l in grid]
    if len(pen_i_l) == 0:
        return grid
    pen_i = pen_i_l.pop()
    for i in range(grid_x):
        for j in range(grid_y):
            for rot in range(4):
                for ref in range(2):
                    place_shape = rotate_translate_reflect(pen_i, rot, (i, j), ref)
                    if is_valid(place_shape, grid):
                        for x, y in place_shape:
                            grid[x][y] = pen_i
                        res = tile(grid_dim, pen_i_l, grid)
                        if res is not None:
                            return res
                        for x, y in place_shape:
                            grid[x][y] = -1
    pen_i_l.append(pen_i)
    return None

penta = [1, 2, 6, 4, 11, 7, 8, 3]
for i in range(3, len(penta)+1):
    print(f'Solving {i}')
    [print(l) for l in tile((i, 5), penta[:i])]
    

