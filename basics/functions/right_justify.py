# -*- coding: utf-8 -*-
"""
This exercise is from the book "Think Python: How to Think Like a Computer 
Scientist" by Allen B. Downey
"""

def right_justify(string):
    """
    Takes a string as a parameter and prints the string with enough leading 
    spaces so that the last letter of the string is in column 70 of the display.
    
    Example:
    >>> right_justify('monty')
                                                                 monty

    """
    width = 70
    spaces_count = width-len(string)
    spaces = " " * spaces_count
    print(spaces + string)

right_justify("monty")

