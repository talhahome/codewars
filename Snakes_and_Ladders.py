# Introduction
#  	Snakes and Ladders is an ancient Indian board game regarded today as a worldwide classic.
#  	It is played between two or more players on a gameboard having numbered, gridded squares.
#  	A number of "ladders" and "snakes" are pictured on the board, each connecting two specific board squares.

# Task
#  	Your task is to make a simple class called SnakesLadders.
#  	The test cases will call the method play(die1, die2) independantly of the state of the game or the player turn.
#  	The variables die1 and die2 are the die thrown in a turn and are both integers between 1 and 6.
#  	The player will move the sum of die1 and die2.

# Rules
# 1.  There are two players and both start off the board on square 0.
#
# 2.  Player 1 starts and alternates with player 2.
#
# 3.  You follow the numbers up the board in order 1=>100
#
# 4.  If the value of both die are the same then that player will have another go.
#
# 5.  Climb up ladders. The ladders on the game board allow you to move upwards and get ahead faster.
# If you land exactly on a square that shows an image of the bottom of a ladder,
# then you may move the player all the way up to the square at the top of the ladder.
# (even if you roll a double).
#
# 6.  Slide down snakes. Snakes move you back on the board because you have to slide down them.
# If you land exactly at the top of a snake,
# slide move the player all the way to the square at the bottom of the snake or chute.
# (even if you roll a double).
#
# 7.  Land exactly on the last square to win. The first person to reach the highest square on the board wins.
# But there's a twist!
# If you roll too high, your player "bounces" off the last square and moves back.
# You can only win by rolling the exact number needed to land on the last square.

# For example, if you are on square 98 and roll a five,
# move your game piece to 100 (two moves), then "bounce" back to 99, 98, 97 (three, four then five moves.)

############################################################
# Solution.
############################################################


class SnakesLadders(object):
    turn = 1
    player1 = 0
    player2 = 0
    # Dictionary for Snakes and Ladders.
    dict = {2: 38,
            7: 14,
            8: 31,
            15: 26,
            16: 6,
            21: 42,
            28: 84,
            36: 44,
            46: 25,
            49: 11,
            51: 67,
            62: 19,
            64: 60,
            71: 91,
            74: 53,
            78: 98,
            87: 94,
            89: 68,
            92: 88,
            95: 75,
            99: 80}
    # Switch for checking if the game is over.
    game_over = False

    def __init__(self):
        pass

    def play(self, die1, die2):
        if self.game_over:
            print("Game over!")
            return "Game over!"
        place = die1 + die2
        # Calculate player's new position.
        if self.turn == 1:
            self.player1 = self.move(self.player1 + place)
            msg = self.check_status(self.player1, self.turn)
            self.check_turn(die1, die2)
            print(msg)
            return msg
        else:
            self.player2 = self.move(self.player2 + place)
            msg = self.check_status(self.player2, self.turn)
            self.check_turn(die1, die2)
            print(msg)
            return msg

    def move(self, position):           # Snake / Ladders / Bounce.
        if position > 100:              # Check if bounce.
            position = 200 - position
        if position in self.dict:       # Check if Snake or Ladders.
            return self.dict[position]
        return position

    def check_status(self, position, turn):     # Check game status if game is over.
        if position == 100:
            self.game_over = True
            return "Player " + str(turn) + " Wins!"
        else:
            return "Player " + str(turn) + " is on square " + str(position)

    def check_turn(self, die1, die2):            # Select which player's turn next.
        if die1 != die2:
            if self.turn == 1:
                self.turn = 2
            else:
                self.turn = 1


game = SnakesLadders()

game.play(6, 6)
game.play(2, 1)
game.play(2, 1)
game.play(1, 1)
game.play(2, 1)
game.play(2, 1)
game.play(3, 3)
game.play(2, 1)

############################################################
# Test Cases.
############################################################
# import random
# test.describe("Random tests")
#
# class SnakesLadders2():
#
#     def __init__(self):
#         self.player_square = []
#         self.player_square.append(0)
#         self.player_square.append(0)
#         self.player = 0
#         self.won = False
#         self.trap = [[2,38],[7,14],[8,31],[15,26],[21,42],[28,84],[36,44],[51,67],[71,91],[78,98],[87,94],
#                     [16,6],[46,25],[49,11],[62,19],[64,60],[74,53],[89,68],[92,88],[95,75],[99,80]]
#
#     def play(self, die1, die2):
#         if self.won: return "Game over!"
#         roll = die1 + die2
#         if roll + self.player_square[self.player] <= 100:
#             self.player_square[self.player] = self.player_square[self.player] + roll
#             if self.player_square[self.player] == 100:
#                 self.won = True
#                 return "Player {wonplayer} Wins!".format(wonplayer=self.player+1)
#         else:
#             self.player_square[self.player] = 100 - ((self.player_square[self.player] + roll) - 100)
#         for t in range(len(self.trap)):
#             if self.player_square[self.player] == self.trap[t][0]:
#                 self.player_square[self.player] = self.trap[t][1]
#             message = "Player "+str(self.player+1)+" is on square "+str(self.player_square[self.player])
#         if die1 != die2:
#             if self.player == 0:
#                 self.player = 1
#             else:
#                 self.player = 0
#         return message
#
# for rtest in range(5):
#     tgame = SnakesLadders2()
#     game = SnakesLadders()
#     for games in range(50):
#         x = random.randint(1,6)
#         y = random.randint(1,6)
#         solution = tgame.play(x, y)
#         test.it("Should return: "+solution)
#         test.assert_equals(game.play(x, y), solution)
