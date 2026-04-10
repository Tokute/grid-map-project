# grid_map is the map of the level or stage
grid_map = []

def createMap(row, column):
    grid_map = [[0 for _ in range(column)] for _ in range(row)]
    return grid_map

def setOuterLimit():
    for i in range(row):
        for j in range(column):
            if (i == 0 or i == row-1):
                grid_map[i][j] = 2

            if (j == 0 or j == column-1):
                grid_map[i][j] = 2
    return grid_map

def showMap():
    for row in grid_map:
        for element in row:
            print(element, end=" ")
        print("")

def setPlayerLocation():
    grid_map[row//2][column//2] = 1

    return grid_map

def getPlayerLocation(): # returns 2 values: row, column
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
            
def isLocationValid(playerRow, playerCol):
    if (((playerRow == 0) or (playerRow == row-1)) or ((playerCol == 0) or (playerCol == column-1))):
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

while True:
    row = int(input("What will be the number of rows for this map: "))
    column = int(input("What will be the number of columns for this map: "))

    if ((row >= 2) and (column >= 2)):
        break
    elif (row < 3):
        print("Error! row must be greater than 2.")
    elif (column < 3):
        print("Error! column must be greater than 2.")

grid_map = createMap(row, column)
grid_map = setOuterLimit()
grid_map = setPlayerLocation()
showMap()

playerRow, playerColumn = getPlayerLocation()
print(f"Player is at [{playerRow}][{playerColumn}]")

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

    
    newRow, newCol = getPlayerLocation()
    if (isLocationValid(newRow, newCol)):
        showMap()
        print("Player is still alive")
    else:
        grid_map[newRow][newCol] = 2
        showMap()
        print("Player hit the grid. Player has died.")