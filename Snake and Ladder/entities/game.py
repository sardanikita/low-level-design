from entities.dice import dice
from entities.player import player
from entities.board import board
from entities.snake import snake
from entities.ladder import ladder


class game:
    def __init__(self):
        self.board = None
        self.dice = None
        self.players = []
        self.turn = 0
        self.last_rank = 0
        self.winner = None
        self.consecutive_six = 0

    def initialize_game(self, board, dice_sides, players_number):

        self.board = board
        self.dice = dice(dice_sides)
        self.players = [player(i) for i in range(players_number)]

    def can_play(self):
        if self.last_rank != len(self.players):
            return True
        return False

    def get_next_player(self):
        """
      Return curr_turn player but if it has already won/completed game , return
      next player which is still active
      """
        while True:
            # if rank is -1 , player is still active so return
            if self.players[self.turn].get_rank() == -1:
                return self.players[self.turn]
            # check next player
            self.turn = (self.turn + 1) % len(self.players)

    def move_player(self, curr_player, next_pos):
        # Move player to next_pos
        curr_player.set_pos(next_pos)
        if self.board.is_last_pos(curr_player.get_pos()):
            # if at last position set rank
            curr_player.set_rank(self.last_rank + 1)
            self.last_rank += 1

    def can_move(self, curr_player, to_move_pos):
        # check if player can move or not ie. between board bound
        if to_move_pos <= self.board.get_size() and curr_player.get_rank() == -1:
            return True
        return False

    def change_turn(self, dice_result):
        # change player turn basis dice result.
        # if it's six, do not change .
        # if it's three consecutive sixes or not a six, change
        self.consecutive_six = 0 if dice_result != 6 else self.consecutive_six + 1
        if dice_result != 6 or self.consecutive_six == 3:
            if self.consecutive_six == 3:
                print("Changing turn due to 3 consecutive sixes")
            self.turn = (self.turn + 1) % len(self.players)
        else:
            print(f"One more turn for player {self.turn + 1} after rolling 6")

    def play(self):
        """
      starting point of game
      game will be player until all players have not been assigned a rank
      # get curr player to play
      # roll dice
      # get next pos of player
      # see if pos is valid to move
      # move player to next pos
      # change turn
      Note: Currently everything is automated, ie. dice roll input is not taken from user.
      if required , we can change that to give some control to user.
      """
        while self.can_play():
            curr_player = self.get_next_player()
            player_input = input(
                f"Player {self.turn + 1}, Press enter to roll the dice")
            dice_result = self.dice.roll()
            print(f'dice_result: {dice_result}')
            _next_pos = self.board.get_next_pos(
                curr_player.get_pos() + dice_result)
            if self.can_move(curr_player, _next_pos):
                self.move_player(curr_player, _next_pos)
            self.change_turn(dice_result)
            self.print_game_state()
        self.print_game_result()

    def print_game_state(self):
        # Print state of game after every turn
        print('-------------game state-------------')
        for ix, _p in enumerate(self.players):
            print(f'Player: {ix + 1} is at pos {_p.get_pos()}')
        print('-------------game state-------------\n\n')

    def print_game_result(self):
        # Print final game result with ranks of each player
        print('-------------final result-------------')
        for _p in sorted(self.players, key=lambda x: x.get_rank()):
            print(f'Player: {_p._id + 1} , Rank: {_p.get_rank()}')


def sample_run():
    # a simple flow of the game
    # here we create a board of size 10 and dice of side 6
    # set snake at 5 with end at 2
    # set ladder at 4 with end at 6
    gboard = board(10)
    gboard.set_board_entity(7, snake(0,2))
    gboard.set_board_entity(4, ladder(0,6))
    game1 = game()
    game1.initialize_game(gboard, 6, 2)
    game1.play()


sample_run()
