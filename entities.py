class Entity:
    """
    The blueprint for entitities appearing in the map.

    Args:
    id (int): id number for identification
    name (str): name for identification
    unicode (char): what unicode it uses to be printed on
    """
    def __init__(self, entity_id, name, unicode):
        self.entity_id = entity_id
        self.name = name
        self.unicode = unicode

class BlankSpace(Entity):
    def __init__(self):
        super().__init__(entity_id=0, name="Blank Space", unicode=chr(0x2B1B))

class Player(Entity):
    def __init__(self, player_name):
        super().__init__(entity_id=1, name=player_name, unicode=chr(0x2705))
        self.health = 100

class KillZone(Entity):
    def __init__(self):
        super().__init__(entity_id=2, name="Kill Zone", unicode=chr(0x1F536))
