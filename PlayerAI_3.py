# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:30:06 2019

@author: jwrose
"""

from random import randint
from BaseAI_3 import BaseAI

class PlayerAI(BaseAI):
    def getMove(self, grid):
        moves = grid.getAvailableMoves()
        return moves[randint(0, len(moves) -1)] if moves else None
    