grid_map = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

grid_map[2][2] = 1 # initial player location

def setOuterLimit():
    for row in range(5):
        for column in range(5):
            if (row == 0 or row == 4):
                grid_map[row][column] = 2

            if (column == 0 or column == 4):
                grid_map[row][column] = 2

def showMap():
    for row in range(5):
        for column in range(5):
            print(f"{grid_map[row][column]}", end=" ")
        print("")

def getPlayerLocation(): # returns 2 values: row, column
    for row in range(5):
        for column in range(5):
            if grid_map[row][column] == 1:
                return row, column
            
def isLocationValid(playerRow, playerCol):
    if (((playerRow == 0) or (playerRow == 4)) or ((playerCol == 0) or (playerCol == 4))):
        return False
    else:
        return True

def moveUp(lastRow, lastCol):
    grid_map[lastRow][lastCol] = 0
    grid_map[lastRow-1][lastCol] = 1

def moveDown(lastRow, lastCol):
    grid_map[lastRow][lastCol] = 0
    grid_map[lastRow+1][lastCol] = 1

def moveRight(lastRow, lastCol):
    grid_map[lastRow][lastCol] = 0
    grid_map[lastRow][lastCol+1] = 1

def moveLeft(lastRow, lastCol):
    grid_map[lastRow][lastCol] = 0
    grid_map[lastRow][lastCol-1] = 1

# main program below

#showMap()
setOuterLimit()
#print("Set Outer Limit Successful")
showMap()

newRow, newCol = getPlayerLocation()

while (isLocationValid(newRow, newCol)):
    lastRow, lastCol = getPlayerLocation()

    playerMovement = input("Where would you like to go (w/a/s/d): ").lower()
    match (playerMovement):
        case 'w':
            moveUp(lastRow, lastCol)
        case 's':
            moveDown(lastRow, lastCol)
        case 'd':
            moveRight(lastRow, lastCol)
        case 'a':
            moveLeft(lastRow, lastCol)
        case _:
            print("Error, invalid movement input.")

    showMap()
    newRow, newCol = getPlayerLocation()
    if (isLocationValid(newRow, newCol)):
        print("Player is still alive")
    else:
        print("Player hit the grid. Player has died.")