#!/usr/bin/env python
# -*- coding: utf-8 -*-

from component import *

SYMBOL = '|'
NAME = "Paddle"

class Paddle(Component):
    """Creates a new paddle.

    Attributes:
        x (int): The X-Axis of the paddle.
        y (int): The Y-Axis of the paddle.
        paddle_id (str): The ID of the paddle.
        size (int): The size of the paddle.
        color (str): The color of the paddle.

    """

    def __init__(self, x, y, paddle_id, size, color):
        super(self.__class__, self).__init__(x, y, self.SYMBOL, color)
        self.paddle_id = paddle_id
        self.size = size
        self.direction = 1 # -1: up; 1: down; 0 fix

    def __str__(self):
        """Prints the paddle.

        Returns:
            str: The paddle.

        """
        return str(self.color + self.SYMBOL + self.DEFAULT_COLOR)

    def __repr__(self):
        """Represents the paddle.

        Returns:
            str: The paddle.

        """
        return str(self.color + self.SYMBOL + self.DEFAULT_COLOR)

    def move(self):
        """Moves the paddle."""
        self.y += self.direction
