def up(grid_map, lastRow, lastCol):
    grid_map[lastRow][lastCol] = 0
    grid_map[lastRow-1][lastCol] = 1

def down(grid_map, lastRow, lastCol):
    grid_map[lastRow][lastCol] = 0
    grid_map[lastRow+1][lastCol] = 1

def right(grid_map, lastRow, lastCol):
    grid_map[lastRow][lastCol] = 0
    grid_map[lastRow][lastCol+1] = 1

def left(grid_map, lastRow, lastCol):
    grid_map[lastRow][lastCol] = 0
    grid_map[lastRow][lastCol-1] = 1