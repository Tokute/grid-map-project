grid_map = []

def createMap(row, column):
    """
        Creates the map from two arguments(row, column)

        Args:
            row (int): num of rows
            column (int): num of columns

        Returns:
            grid_map (2d List): filled with zeros with rows and columns based on the args
    """
    grid_map = [[0 for _ in range(column)] for _ in range(row)]
    return grid_map

def setOuterLimit(grid_map):
    """
        Sets the outer limit of the grid_map

        No args

        Returns:
            grid_map (2d List): grid_map with 2s on the edge
    """
    row = len(grid_map)
    column = len (grid_map[0])
    for i in range(row):
        for j in range(column):
            if (i == 0 or i == row-1):
                grid_map[i][j] = 2

            if (j == 0 or j == column-1):
                grid_map[i][j] = 2
    return grid_map

def showMap(grid_map, render=False):
    """
        Prints out the grid_map
        
        Args:
            render (bool): determines if the function will print pure integers or unicode

        No Returns
    """

    if not render:
        for row in grid_map:
            for element in row:
                print(element, end=" ")
            print("")
    else:
        for row in grid_map:
            for element in row:
                match (element):
                    case 0: # Free space (black square emoji)
                        print(chr(0x2B1B), end=" ")
                    case 1: # Player space (checkmark emoji)
                        print(chr(0x2705), end=" ")
                    case 2: # Outer/Killzone space (red diamond emoji)
                        print(chr(0x1F536), end=" ")
                    case 3: # Death space (SOS emoji)
                        print(chr(0x1F198), end=" ")
                    case _: # if unknown/unassigned integer, print integer itself
                        print(element, end=" ")
            print("")