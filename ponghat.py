#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '/usr/lib/python2.7/dist-packages/sense_hat')

from sense_hat import SenseHat

from src.ai import *
from src.ball import *
from src.ground import *
from src.paddle import *

import time
import os

YELLOW = "\033[1;33m"
sense = SenseHat()
sense.low_light = True

def display_info(fps, time_start, time_elapsed):
    """Gets information about the game.

    Args:
        fps (float): The frames per second of the game.
        time_start (float): The time start for the processus.
        time_elapsed (float): The time elapsed for the processus.

    """
    print(' ' * 5 + '[ Game Info ]' + ' ' * 5 + '\n' * 2
         + 'FPS: ' + str(fps) + '\n'
         + 'Time Elapsed: ' + str(time_elapsed) + '\n'
         + 'Time Start: ' + str(time_start) + '\n')

def render(ground):
    """Renders the game.

    Args:
        ground (Ground): The ground of the game.

    Returns:
        Tuple(bool, bool): Tells if the ball is out and if there is a
        winner.

    """
    game = ground.update()
    print_array(ground.array)
    time.sleep(ground.ball.speed)
    ground.ball.speed = ground.ball.initial_speed
    os.system('clear')
    return game

def print_array(array):
    """Displays an array.

    Args:
        list: The array.

    """
    for j in range(len(array)):
       for i in range(len(array)):
          if array[i][j] == 0:
             sense.set_pixel(j, i, [0, 0, 0])
          elif isinstance(array[i][j], Ball):
             sense.set_pixel(j, i, [255,255,255])
          else:
             sense.set_pixel(j, i, [173, 0, 0])

def start():
    """Starts the game."""
    level = 1
    frames = []
    time_start = time.process_time()
    game = True

    sense.show_message("PyPong")
    time.sleep(0.2)
    sense.show_message("3")
    time.sleep(0.1)
    sense.show_message("2")
    time.sleep(0.1)
    sense.show_message("1")
    time.sleep(0.1)
    sense.show_message("Go!")

    player1 = 0
    player2 = 0

    speed = 0.6
    games = 0

    while (player1 != 3 and player2 != 3):
        games += 1
        ball = Ball(4, 4, 1, speed, YELLOW)
        ground = Ground(8, 8, ball, level)
        sense.stick.direction_up = ground.pushed_up
        sense.stick.direction_down = ground.pushed_down
        game_is_on = True
        while (game_is_on):
            game_is_on, result = render(ground)
            if game_is_on:
                time_end = time.process_time()
                time_elapsed = time_end - time_start

                time_start = time_end

                frames.append(time_elapsed)
                frames = frames[-20:]
                fps = len(frames) / sum(frames)

        if level < 3:
            sense.show_message(str(result))
            sense.show_message('points')
            if games == 3:
               level += 1
               speed -= 0.01
               games = 0
               sense.show_message('Level ' + str(level) + '!')
        else:
            if result == 1:
               player1 = player1 + 1
            else:
               player2 = player2 + 1
            sense.show_message(str(player1) + ':' + str(player2))
        speed -= 0.02

        time.sleep(1)
    sense.show_message("End")

start()
