# Copyright 2013 Gary Baumgartner
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Fall 2013.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
# Edited by: Matthew Kim
"""
DomainStools:  Model Anne Hoy's stools holding cheeses.
Cheese:   Model a cheese with a given size
"""

class DomainStools:
    
    """Model Anne Hoy's stools holding cheese.

    Model stools holding stacks of cheese, enforcing the constraint
    that a larger cheese may not be placed on a smaller one.
    """
    
    
    
    def __init__ (self: 'DomainStools', number_of_stools: 'int'):
        
        self.number_of_stools = number_of_stools
        self.number_of_moves = 0
        self.cheeses = [[], [], [], []]

    # TODO: See Steps 2 and 3 of the handout.

    def move(self: 'DomainStools', cheese_to_move:
             'Cheese', cheese: 'Cheeseview') -> None:
        
        if(cheese.size < cheese_to_move.size):
            raise TooBigException
        if(not cheese == self.cheeses[cheese.stool][-1] or \
           not cheese_to_move == self.cheeses[cheese_to_move.stool][-1]):
            raise NotTopCheese
        if(len(self.cheeses[cheese_to_move.stool]) <=1):
            raise IsStool
        self.cheeses[cheese_to_move.stool].pop()
        self.add(cheese.stool, cheese_to_move)
        self.number_of_moves += 1

    def add(self: 'DomainStools', stool: 'Stool',
            cheese: 'Cheese') -> None:
        
        self.cheeses[stool].append(cheese)
        cheese.stool = stool


class Cheese:
    def __init__(self: 'Cheese', size: float) -> None:
        """
        Initialize a Cheese to diameter size.

        >>> c = Cheese(3)
        >>> isinstance(c, Cheese)
        True
        >>> c.size
        3
        """

        self.size = size
        self.stool = 0


class TooBigException(Exception):
    
    def __init__(self: 'TooBigException'):
        self.super(TooBigException, self).__init__('Cheese is too big to move')


class NotTopCheese(Exception):
    
    def __init__(self: 'NotTopCheese'):
        self.super(NotTopCheese, self).__init__('Cheese is not on top')


class IsStool(Exception):

    def __init__(self: 'IsStool'):
        self.super(IsStool, self).__init__('This is a Stool')
