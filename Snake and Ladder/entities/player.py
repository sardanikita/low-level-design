class player:
    def __init__(self, _id, name=None):
        self._id = _id
        self.name = name
        self.pos = 1
        self.rank = -1

    def set_rank(self, rank):
        self.rank = rank

    def get_rank(self):
        return self.rank

    def set_pos(self, pos):
        self.pos = pos

    def get_pos(self):
        return self.pos