# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, start_room):
        self._name = "Nameless Hero"
        self._room = start_room

    def name(self):
        return self._name

    def setName(self, new_name):
        self._name = new_name

    def room(self):
        return self._room.name()

    def setRoom(self, new_room):
        self._room = new_room

    def __str__(self):
        return f"My name is {self.name()}, and I'm in the {self.room()}"