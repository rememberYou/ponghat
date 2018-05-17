#!/usr/bin/env python
# -*- coding: utf-8 -*-

from component import *
from random import randrange

SYMBOL = 'o'
NAME = "Ball"

class Ball(Component):
    """Creates a new ball

    Attributes:
        x (int): The X-Axis of the ball.
        y (int): The Y-Axis of the ball.
        side (int): The size of the ball.
        speed (float): The speed of the ball.
        color (str): The color of the ball.

    """

    def __init__(self, x, y, side, speed, color):
        super(self.__class__, self).__init__(x, y, self.SYMBOL, color)
        self.side = side
        self.dx = 0
        self.dy = 0
        t = [-135, 135]
        self.angle = t[randrange(2)]
        self.initial_speed = speed
        self.speed = speed
        self.set_direction()

    def __str__(self):
        """Prints the ball.

        Returns:
            str: The ball.

        """
        return str(self.color + self.SYMBOL + self.DEFAULT_COLOR)

    def __repr__(self):
        """Represents the ball.

        Returns:
            str: The ball.

        """
        return str(self.color + self.SYMBOL + self.DEFAULT_COLOR)

    def set_direction(self):
        """Sets the direction the ball according to an angle.

          dx: vertical   (-1: up; 0: none; 1: down)
          dy: horizontal (-1: left; 0: none; 1: right)

        """
        if self.angle == -135:
            self.dx = 1
            self.dy = -1
        elif self.angle == -45:
            self.dx = 1
            self.dy = 1
        elif self.angle == 45:
            self.dx = -1
            self.dy = 1
        else:
            self.dx = -1
            self.dy = -1

    def move(self):
        """Moves the ball according to the calculated direction."""
        self.x += self.dx
        self.y += self.dy
