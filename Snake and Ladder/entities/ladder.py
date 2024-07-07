from entities.board_entities import board_entities

class ladder(board_entities):
    def __init__(self, start_pos=None, end_pos=None):
        super(ladder, self).__init__(start_pos, end_pos)
        self.desc = 'Ladder'