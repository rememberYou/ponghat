#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ai import *
from ball import *
from paddle import *

import time

RED = "\033[1;31m"
BLUE = "\033[1;34m"
YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
DEFAULT = "\033[0;0m"
BOLD = "\033[;1m"

class Ground:
    """Creates a new ground.

    Attributes:
        row (int): The X-Axis length of the ground.
        column (int): The Y-Axis length of the ground.
        ball (Ball): The ball of the ground.
        level (int): The level of the ground.

    """

    def __init__(self, row, column, ball, level):
        self.row = row
        self.column = column
        self.ball = ball
        self.level = level
        self.result = 0

        if self.level < 3:
            self.paddle = Paddle((self.row // 2) + 1,
                                 self.column - 2, 'Right', 2, self.RED)
            self.components = [self.ball, self.paddle]
            self.positions = [ball.y, ball.x, self.paddle.y, self.paddle.x]
        else:
            self.paddle_left = Paddle(self.row // 2, 1, 'Left', 2, self.RED)
            self.paddle_right = Paddle((self.row // 2) + 1,
                                      self.column - 2, 'Right', 2, self.CYAN)
            self.components = [self.ball, self.paddle_left, self.paddle_right]
            self.positions = [ball.y, ball.x, self.paddle_left.y, self.paddle_left.x,
                                              self.paddle_right.x, self.paddle_right.y]
            self.ai = AI(self.paddle_left)

        self.array = self.generate_ground(row, column)
        self.init_components(self.components)

    def __str__(self):
        """Prints the ground.

        Returns:
            str: The ground.

        """
        return str(self.array[i])

    def clean_positions(self):
        """Removes the old positions of the components."""
        self.array[self.positions[0]][self.positions[1]] = 0
        self.array[self.positions[2]][self.positions[3]] = 0

        if self.level == 3:
            self.array[self.positions[4]][self.positions[5]] = 0

    def debug(self, components):
        """Debugs by displaying X-Axis and Y-Axis of components.

        Args:
            components: The list of components.

        """
        print(' ' * 5 + '[ Debug Mode ]' + ' ' * 5 + '\n')
        for component in components:
            print(component.NAME + "(x=" + str(component.x)
                                 + ", y=" + str(component.y) + ")")
        print('\n')

    def generate_ground(self, row, column):
        """Generates the ground.

        Args:
            row (int): The rows for the ground.
            column (int): The columns for the ground.

        Returns:
            list: The ground.

        """
        return [[0 for i in range(row)] for j in range(column)]

    def init_components(self, components):
        """Initializes the components in the array.

        Args:
            components (list): The list of components.

        """
        for component in components:
            self.array[component.x][component.y] = component

    def is_winner(self):
        """Tells the result of the current game.

        Returns:
            int: The score if the level is lower than 3, 1 if the first
            player wins, 2 for the second.

        """
        if self.level < 3:
            return self.result
        if self.ball.y < 0:
            return 2
        elif self.ball.y > 7:
            return 1

    def is_paddle_collision(self):
        """Upgrade the direction of the ball and the score if there is
        a collision with a paddle.

        """
        if self.level < 3:
            if self.ball.y == self.column - 2 and self.ball.x == self.paddle.x:
                self.ball.dy = -self.ball.dy
                self.result += 2
                self.ball.speed -= 0.15
        else:
            if (self.ball.y == 1 and self.ball.x == self.paddle_left.x) or \
               (self.ball.y == self.column - 2 and self.ball.x == self.paddle_right.x):
                self.ball.dy = -self.ball.dy
                self.ball.speed -= 0.15

    def is_out(self):
        """Detects if the ball is out of bounds.

        Returns:
            bool: true if the ball is out of bounds; false otherwise.

        """
        if self.level < 3:
            return self.ball.y == self.column - 1
        return self.ball.y == 0 or self.ball.y == self.column - 1

    def is_wall_collision(self):
        """Detects if there is a collision with the ball and the bottom
        or top of the wall or with the right side of the ground.

        """
        if self.level < 3:
            if self.ball.x == 0 or self.ball.x == self.row - 1:
                # Roof
                self.ball.dx = -self.ball.dx
                self.result += 3
                self.ball.speed -= 0.1
            if self.ball.y == 0:
                # Left side
                self.ball.dy = -self.ball.dy
                self.result += 3
                self.ball.speed -= 0.1
        else:
            if self.ball.x == 0 or self.ball.x == self.row - 1:
                # Roof
                self.ball.dx = -self.ball.dx
                self.ball.speed -= 0.1

    def pushed_up(self):
        """If the joystick of the Sense HAT is pushed up, the paddle is
        moved upwards.

        """
        self.stick_move = -1

    def pushed_down(self):
        """If the joystick of the Sense HAT is pushed down, the paddle
        is moved downwards.

        """
        self.stick_move = 1

    def move_paddle(self, move):
        """Verifies if the paddle can move. If it can, it'll from the
        direction given by the Sense HAT.

        Args:
            move (int): The shift in motion

        """
        if self.level < 3:
            if not ((self.paddle.x == 0 and self.stick_move == -1) or \
                    (self.paddle.x == self.row-1 and self.stick_move == 1)):
                self.paddle.x += move
        else:
            if not ((self.paddle_right.x == 0 and self.stick_move == -1) or \
                    (self.paddle_right.x == self.row-1 and self.stick_move == 1)):
                self.paddle_right.x += move

    def update(self):
        """Updates the game.

        Returns:
            Tuple(bool, bool): Tells if the ball is out and if there is
            a winner.

        """
        self.clean_positions()
        out = True

        if self.is_out():
            out = False

        if self.level < 3:
            self.move_paddle(self.stick_move)

            if out:
                self.is_wall_collision()
                self.is_paddle_collision()

            self.positions[0] = self.ball.x
            self.positions[1] = self.ball.y

            self.positions[2] = self.paddle.x
            self.positions[3] = self.paddle.y

            self.array[self.positions[2]][self.positions[3]] = self.paddle
        else:
            self.move_paddle(self.stick_move)

            self.is_wall_collision()
            self.is_paddle_collision()

            self.positions[0] = self.ball.x
            self.positions[1] = self.ball.y

            self.positions[2] = self.paddle_left.x
            self.positions[3] = self.paddle_left.y
            self.positions[4] = self.paddle_right.x
            self.positions[5] = self.paddle_right.y

            self.array[self.positions[2]][self.positions[3]] = self.paddle_left
            self.array[self.positions[4]][self.positions[5]] = self.paddle_right

        self.array[self.positions[0]][self.positions[1]] = self.ball

        self.ball.move()

        if self.level == 3:
            self.ai.play(self.ball, self.paddle_left)
            winner = self.is_winner()
        else:
            winner = self.is_winner()

        self.stick_move = 0

        return out, winner
