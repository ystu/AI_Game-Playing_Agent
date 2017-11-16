"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    def test1(self):
        a = 2
        b = 1
        # self.assertTrue(a == b, "ffalse")
        print('a = ', a)
        print(self.game.get_legal_moves(self.player1))






if __name__ == '__main__':
    unittest.main()
