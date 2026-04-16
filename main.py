import keyboard
import time
import os
import mapTools
import locationTools
import playerTools
# grid_map is the map of the level or stage
# TO DO: Try to learn about OOP or refactor the entire program before developing next ideas
"""
Ideas:
    Dynamic Map Shapes
        this will make each grid_map dynamic with different or combined shapes
        currently dont have any idea how can I do this, will need research

    Randomly Generated Structures/Objects
        this will generate random integers on the 0s, these integers will represent objects that the player will need
        or something

    Goal/Enter Room Condition
        Maybe set a random location or somewhere in the outer limits to maybe number 4. 4 basically means if the player
        manages to reach this index, they will advance to another room.
        (This project is gonna need more handling on more grid_maps)
"""

"""
while True:
    This was before adding generateMap()
    row = int(input("What will be the number of rows for this map: "))
    column = int(input("What will be the number of columns for this map: "))

    if ((row >= 2) and (column >= 2)):
        break
    elif (row < 3):
        print("Error! row must be greater than 2.")
    elif (column < 3):
        print("Error! column must be greater than 2.")
    """

def determineEvent(indexValue):
    """
        Determines what event depending on the integer passed onto this function.
    """
    eventIntegers = {
        0: "FREE",
        1: "PLAYER",
        2: "DEATH",
        3: "DEATH_LOC",
        4: "NEW_ROOM"
    }

    if (indexValue) in eventIntegers:
        print(eventIntegers[indexValue])
        return eventIntegers[indexValue]
    else:
        return "Unregistered or invalid event: {}".format(indexValue)

def applyEvent(event):
    """
        Applies the event, complements determineEvent(). This function needs to return True if player is alive.
    """
    global grid_map
    if (event == "DEATH"):
        return False
    elif (event == "NEW_ROOM"):
        grid_map = mapTools.generateMap()
        grid_map = locationTools.setPlayerLocation(grid_map)
        return True


    return True

#grid_map = mapTools.createMap(row, column)
grid_map = mapTools.generateMap()
grid_map = locationTools.setPlayerLocation(grid_map)
mapTools.showMap(grid_map)

playerRow, playerColumn = locationTools.getPlayerLocation(grid_map)
print(f"Player is at [{playerRow}][{playerColumn}]")

key_states = {"w": False, "a": False, "s": False, "d": False}
alive = True
event = ""

while alive:
    lastRow, lastCol = locationTools.getPlayerLocation(grid_map)
    #print(f"Last Row: {lastRow}, Last Column: {lastCol}")

    #alive = applyEvent(event)

    moved = False
    for key in key_states:
        if keyboard.is_pressed(key):
            if not key_states[key]:
                try:
                    event = determineEvent(playerTools.checkNextIndex(grid_map, key))
                    match key:
                        case 'w': playerTools.up(grid_map)
                        case 's': playerTools.down(grid_map)
                        case 'a': playerTools.left(grid_map)
                        case 'd': playerTools.right(grid_map)
                except IndexError as ie:
                    print("Error index invalid.")

                moved = True
                key_states[key] = True
                alive = applyEvent(event)
                break
        else:
            key_states[key] = False

    if moved:
        os.system('cls' if os.name == 'nt' else 'clear')
        mapTools.showMap(grid_map)
        playerRow, playerColumn = locationTools.getPlayerLocation(grid_map)
        print(f"Player is at [{playerRow}][{playerColumn}]")
        #newRow, newCol = getPlayerLocation()

    if keyboard.is_pressed("esc"):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Menu Screen")
        break

    time.sleep(0.05)

lastRow, lastCol = locationTools.getPlayerLocation(grid_map)
os.system('cls' if os.name == 'nt' else 'clear')
grid_map[lastRow][lastCol] = 3
mapTools.showMap(grid_map)
print("Player hit the grid. Player has died")
