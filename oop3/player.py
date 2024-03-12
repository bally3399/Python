class Player:
    def __init__(self, name, cell):
        self._name = name
        self._cell = cell

    @property
    def name(self):
        return self._name

    @property
    def cell(self):
        return self._cell
