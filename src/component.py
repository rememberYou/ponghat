#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

DEFAULT_COLOR = '\033[0;0m'

class Component(ABC):
    """Creates a new component.

    Attributes:
        x (int): The X-Axis of the component.
        y (int): The Y-Axis of the component.
        symbol (str): The symbol of the component.
        color (str): The color of the component.

    """

    def __init__(self, x, y, symbol, color):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.color  = color

    def __str__(self):
        """Prints the component.

        Returns:
            str: The component.

        """
        return str(self.color + self.SYMBOL + self.DEFAULT_COLOR)

    def __repr__(self):
        """Represents the component.

        Returns:
            str: The component.

        """
        return str(self.color + self.SYMBOL + self.DEFAULT_COLOR)

    @abstractmethod
    def move(self):
        """Moves the component according to the X-Axis and Y-Axis."""
        pass
