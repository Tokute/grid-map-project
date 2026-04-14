def setPlayerLocation(grid_map):
    """
        Sets the player location on the middle of the grid_map

        Args:
            grid_map (2d List): map to scan

        Returns:
        grid_map (2d List): grid_map with a number 1 on the middle
    """
    row = len(grid_map)
    column = len (grid_map[0])
    grid_map[row//2][column//2] = 1

    return grid_map

def getPlayerLocation(grid_map): # returns 2 values: row, column
    """
        Loops through grid_map to find where the player (1) is located

        Args:
            grid_map (2d List): grid_map it will scan

        Returns:
            foundRow (int): row index of player location
            foundColumn (int): row column of player location
    """
    row = len(grid_map)
    column = len (grid_map[0])

    playerFound = False
    for i in range(row):
        for j in range(column):
            if grid_map[i][j] == 1:
                playerFound = True
                foundRow, foundColumn = i, j
    
    if (playerFound):
        return foundRow, foundColumn
    else:
        return -1, -1
            
def isLocationValid(grid_map, playerRow, playerCol):
    """
        Checks if the location of the player is not within the outer limits

        Args:
            playerRow (int)
            playerCol (int)

        Returns:
            True or False
    """
    row = len(grid_map)
    column = len (grid_map[0])
    if (((playerRow == 0) or (playerRow == row-1)) or ((playerCol == 0) or (playerCol == column-1))):
        return False
    else:
        return True