# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):

        self._name = name
        self._description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def name(self):
        return self._name

    def description(self):
        return self._description