This small project basically uses a 2d list to to show the playable area. This must not have any good reasons or causes but I wanna try making a small program that takes in my current coding knowledge from my first year of CS and basically the progress of my learnings.

roomTraversal branch is for improving most of locationTools and to make Room Traversal possible with generateMap(). In the previous commits of this program, the code checks if the player has 'stepped' on the outer limits of the grid_map. Now this branch will implement that it will just check if the player stepped on 2 in the 2d list.

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