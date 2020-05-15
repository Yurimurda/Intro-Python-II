# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __str__(self):
        return self.name, self.description


# outside = Room("Outside Cave Entrance", "North of you, the cave mount beckons")
# foyer = Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""")
# overlook = Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""")
# narrow = Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""")
# treasure = Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""")

# Room['outside'].n_to = Room['foyer']
# Room['foyer'].s_to = Room['outside']
# Room['foyer'].n_to = Room['overlook']
# Room['foyer'].e_to = Room['narrow']
# Room['overlook'].s_to = Room['foyer']
# Room['narrow'].w_to = Room['foyer']
# Room['narrow'].n_to = Room['treasure']
# Room['treasure'].s_to = Room['narrow']