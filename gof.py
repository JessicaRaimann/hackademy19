import random

def setup_game(size, max_alive):
    a_grid = get_empty_grid(size)
    fill_grid_random(a_grid, max_alive) #it fills the empty grid randomly with the mxaimum of cells alive

def get_empty_grid(size):
    new_grid = []
    for row in range(size):
        new_list = []
        for column in range(size):
            new_list.append('-')
        new_grid.append(new_list)
    return new_grid

def rand_alive():
    number = random.randint(1,3)
    if number == 1:
        return True
    else:
        return False

def fill_grid_random(a_grid,max_alive):
    size = len(a_grid)
    remaining = max_alive
    for r_i in range(size):
        for c_i in range(size): #change the content of a list in a list
            if (rand_alive() == True) and (remaining > 0):
                a_grid[r_i][c_i] = 'X'
                remaining = remaining - 1
            else:
                a_grid[r_i][c_i] = '-'
    return a_grid

def print_grid(a_grid):
    size = len(grid)
    for r_i in range(size):
        for c_i in range(size):
            print(a_grid[r_i, c_i], end='')
        print('')

grid = get_empty_grid(10)
fill_grid_random(grid,10)
print_grid(grid) #grid is filled now



