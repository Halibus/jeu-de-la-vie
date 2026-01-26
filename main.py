import time, os, copy

grid = [
    [1, 0],
    [0, 1],
    [0],
    [0],
    [0],
    [0],
    [0],
]

H, W = len(grid), len(grid[0])

def neighbors(g, x, y):
    s = 0
    for i in (-1,0,1):
        for j in (-1,0,1):
            if i == 0 and j == 0: 
                continue
            nx, ny = x+i, y+j
            if 0 <= nx < H and 0 <= ny < W:
                s += g[nx][ny]
    return s

while True:
    os.system("clear")
    for row in grid:
        print("".join("█" if c else " " for c in row))
    time.sleep(1)

    new = copy.deepcopy(grid)
    for i in range(H):
        for j in range(W):
            n = neighbors(grid, i, j)
            if grid[i][j] == 1 and n not in (2,3):
                new[i][j] = 0
            elif grid[i][j] == 0 and n == 3:
                new[i][j] = 1
    grid = new

