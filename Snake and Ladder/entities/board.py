class board:
    def __init__(self, size):
        self.size = size
        self.board = {}

    def set_board_entity(self, pos, entity):
        self.board[pos] = entity

    def get_size(self):
        return self.size
    def is_last_pos(self, pos):
        if pos == self.size:
            return True
        return False

    def get_next_pos(self, player_pos):
        # get next pos given a specific position player is on
        if player_pos > self.size:
            return player_pos
        if player_pos not in self.board:
            return player_pos
        return self.board[player_pos].get_end_pos()