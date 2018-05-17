#!/usr/bin/env python
# -*- coding: utf-8 -*-

class AI:
    """Creates a new AI.

    Attributes:
        paddle (Paddle): The AI paddle.

    """

    def __init__(self, paddle):
        self.paddle = paddle

    def distance(self, ball, paddle):
        """Calculates the distance between the paddle and the ball.

        Args:
            ball (Ball): The ball.
            paddle (Paddle): The AI paddle.

        Returns:
            float: The distance between the paddle and the ball.

        """
        return ball.y - paddle.y

    def go_left_up(self, ball, paddle):
        """Verifies if the paddle can go up.

        Args:
            ball (Ball): The ball.
            paddle (Paddle): The AI paddle.

        Returns:
            bool: true if the paddle can go up; false otherwise.

        """
        return ball.x < paddle.x

    def go_left_down(self, ball, paddle):
        """Verifies if the paddle can go down.

        Args:
            ball (Ball): The ball.
            paddle (Paddle): The AI paddle.

        Returns:
            bool: true if the paddle can go down; false otherwise.

        """
        return ball.x > paddle.x

    def debug(self, ball, paddle):
        """Debugs by displaying infos about the AI.

        Args:
            ball (Ball): The ball.
            paddle (Paddle): The AI paddle.

        """
        print(' ' * 5 + '[ AI Mode ]' + ' ' * 5 + '\n')
        if (self.go_left_up(ball, paddle)):
            print('Direction to take: UP')
        else:
            print('Direction to take: DOWN')
        print('Distance from the ball: ' + str(self.distance(ball, paddle)) + '\n')

    def play(self, ball, paddle):
        """Makes the AI play the game.

        Args:
            ball (Ball): The ball.
            paddle (Paddle): The AI paddle.

        """
        if self.paddle.ID == 'Left' and ball.y <= 3:
            if self.go_left_up(ball, paddle):
                paddle.x = paddle.x - 1
            elif self.go_left_down(ball, paddle):
                paddle.x = paddle.x + 1
        elif self.paddle.ID == 'Right' and ball.y >= 3:
            if self.go_left_up(ball, paddle):
                paddle.x = paddle.x - 1
            elif self.go_left_down(ball, paddle):
                paddle.x = paddle.x + 1
