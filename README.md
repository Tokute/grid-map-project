This small project basically uses a 2d list to to show the playable area. This must not have any good reasons or causes but I wanna try making a small program that takes in my current coding knowledge from my first year of CS and basically the progress of my learnings.

Updates:
    OOP has been implemented across the files.

    entities.py:
        entity_id = integer associated/assigned with the object
        name = string name of the object (for documentation or other purposes)
        unicode = unicode to print to the terminal (for print_map function of map_tools)

    location_tools.py:
        shortened get_index_of_intger into get_index
        also adjusted for objects.

    main.py:
        many changes to use objects.
        added initializations of objects.

    map_tools.py:
        many changes (again).
        turned gridmap into a full object for scalability and organization.
        print_map now includes unicode.
        initialize_map now assigns objects instead of integers.

    player_tools.py:
        adjusted accordingly to use objects instead of integers.
        movement logic now condensed into one function instead of 4 separate functions for up, down, left, right.

Ideas:
    main.py:
        Determine event and apply event into one function.
            Since we are already working with objects, determine event might not be needed anymore.
            apply_event could use the entity.name or entity.id or entity class will have a new attribute called event_id.

    Dynamic Map Shapes (Very difficult)
        this will make each grid_map dynamic with different or combined shapes
        currently dont have any idea how can I do this, will need research

    Randomly Generated Structures/Objects
        this will generate random integers on the 0s, these integers will represent objects that the player will need
        or something