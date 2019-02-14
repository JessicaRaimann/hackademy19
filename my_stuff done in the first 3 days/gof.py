import random
from cell import *

def setup_game(size, max_alive):
    a_grid = get_empty_grid(size)
    fill_grid_random(a_grid, max_alive) #it fills the empty grid randomly with the mxaimum of cells alive

def get_empty_grid(size):
    new_grid = []
    for r_i in range(size):
        new_sublist = []
        for c_i in range(size):
            # new_sublist.append('-')
            a_new_cell = Cell(r_i,c_i)
            new_sublist.append(a_new_cell)
        new_grid.append(new_sublist)
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
                a_cell = a_grid[r_i][c_i] #specific sell in a grid and making it alive
                a_cell.make_alive()
                remaining = remaining - 1
#            else:
#                a_grid[r_i][c_i] = '-'
#    return a_grid

def print_grid(a_grid):
    size = len(a_grid)
    print(size)
    for r_i in range(size):
        for c_i in range(size):
           a_cell = a_grid[r_i][c_i]
           a_cell.print_myself()
        print('')

def find_all_neigh(a_grid):
    size = len(a_grid)
    for r_i in range(size):
        for c_i in range(size):
            a_cell = a_grid[r_i][c_i]
            a_cell.find_neigh(a_grid)

def compute_all_ni(a_grid):
    size = len(a_grid)
    for r_i in range(size):
        for c_i in range(size):
            a_cell = a_grid[r_i][c_i]
            a_cell.compute_next_iteration()

def evolve_all(a_grid):
    size = len(a_grid)
    for r_i in range(size):
        for c_i in range(size):
            a_cell = a_grid[r_i][c_i]
            a_cell.evolve()

###Funktionen ausführen

print("Getting empty grid...")
grid = get_empty_grid(8)
print("Finding all the neighbours...")
find_all_neigh(grid)
print("Filling the grid...")
fill_grid_random(grid,8)
print("Printing a grid...")
print_grid(grid)

compute_all_ni(grid)
evolve_all(grid)
print_grid(grid)
