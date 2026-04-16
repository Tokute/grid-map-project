import locationTools

movementLogic = {
        'w': (-1, 0),
        's': (1, 0),
        'd': (0, 1),
        'a': (0, -1)
    }

def up(grid_map):
    lastRow, lastCol = locationTools.getPlayerLocation(grid_map)
    grid_map[lastRow][lastCol] = 0
    grid_map[lastRow-1][lastCol] = 1

def down(grid_map):
    lastRow, lastCol = locationTools.getPlayerLocation(grid_map)
    grid_map[lastRow][lastCol] = 0
    grid_map[lastRow+1][lastCol] = 1

def right(grid_map):
    lastRow, lastCol = locationTools.getPlayerLocation(grid_map)
    grid_map[lastRow][lastCol] = 0
    grid_map[lastRow][lastCol+1] = 1

def left(grid_map):
    lastRow, lastCol = locationTools.getPlayerLocation(grid_map)
    grid_map[lastRow][lastCol] = 0
    grid_map[lastRow][lastCol-1] = 1

def checkNextIndex(grid_map, keyPressed):
    """
        This function checks the next index to get what integer the player is moving to.
    """
    row = len(grid_map)
    column = len(grid_map[0])
    lastRow, lastCol = locationTools.getPlayerLocation(grid_map)
    rowOffset, colOffset = movementLogic[keyPressed]
    targetRow = lastRow + rowOffset
    targetCol = lastCol + colOffset

    if not ((0 <= targetRow <= row) and (0 <= targetCol <= column)):
        raise IndexError("Error Index Out of Bounds")
        #grid_map[lastRow][lastCol] = 0
        #grid_map = locationTools.setPlayerLocation(grid_map)

    return grid_map[targetRow][targetCol]