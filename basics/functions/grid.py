# -*- coding: utf-8 -*-
"""
Think Python: How to Think Like a Computer Scientist
Allen B. Downey

Chapter 3  Functions

Exercise 3  

Note: This exercise should be done using only the statements and other features we have learned so far.

Write a function that draws a grid like the following:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
Hint: to print more than one value on a line, you can print a comma-separated sequence of values:

print('+', '-')
By default, print advances to the next line, but you can override that behavior and put a space at the end, like this:

print('+', end=' ')
print('-')
The output of these statements is '+ -' on the same line. The output from the next print statement would begin on the next line.

Write a function that draws a similar grid with four rows and four columns.
"""

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def draw_horizonlal_line():
    print("+ - - - -", end = " ")

def draw_vertical_line():
    print("|        ", end = " ")
    
def draw_3_vertical_lines():
    do_twice(draw_vertical_line)
    print("|")

def draw_5_vertical_lines():
    do_four(draw_vertical_line)
    print("|")

def draw_row_2_cells():
    do_twice(draw_horizonlal_line)
    print("+")
    do_four(draw_3_vertical_lines)

def draw_row_4_cells():
    do_four(draw_horizonlal_line)
    print("+")
    do_four(draw_5_vertical_lines)

def draw_grid_2x2():
    do_twice(draw_row_2_cells)
    do_twice(draw_horizonlal_line)
    print("+")

def draw_grid_4x4():
    do_four(draw_row_4_cells)
    do_four(draw_horizonlal_line)
    print("+")

draw_grid_2x2()
draw_grid_4x4()



