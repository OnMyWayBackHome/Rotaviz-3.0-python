from graphics import *
#import numpy as np
from math import cos, sqrt, pi
from random import randint


def center_on_zero(block, back=False):
    """
    Subtracts 128 from each element in a matrix so the values are centered on zero
    :param block: 8 x 8 array of pixel values
    :return: 8 x 8 array of each element minus 128
    """
    #return block - np.ones((8,8))*(128)
    centered = []
    for row in block:
        if back:

            centered.append([max([min([x + 128,255]),0]) for x in row])
        else:
            centered.append([x - 128 for x in row])
    return centered

def alpha(x):
    """
    Returns the value of alpha(x) in the DCT
    :param x: row or column of the DCT basis function
    :return: alpha(x)
    """
    if x == 0:
        return 1 / sqrt(2)
    else:
        return 1

def dct(block):
    """
    Returns the discrete cosine transformation of the block
    :param block: 8x8 block of pixel values centered on zero
    :return: dct
    """
    dct = []
    for u in range(8): # u is the column of the basis function
        row = []
        for v in range(8): # v is the row
            sum = 0
            for x in range(8):
                for y in range(8):
                    sum += block[x][y] * cos((2*x + 1) * u * pi/16) * cos((2*y + 1)* v * pi/16)
            row.append(0.25 * alpha(u) * alpha(v) * sum)
        dct.append(row)
    return dct

def inverse_dct(block):
    """
    Returns the inverse discrete cosine transformation of the block
    :param block: 8x8 block of DCT coefficients
    :return: inverse dct
    """
    inv = []
    for x in range(8):
        row = []
        for y in range(8):
            sum = 0
            for u in range(8): # u is the column of the basis function
                for v in range(8): # v is the row
                    sum += alpha(u) * alpha(v) * block[u][v] * cos((2*x + 1) * u * pi/16) * cos((2*y + 1)* v * pi/16)
            row.append(int(0.25 * sum))
        inv.append(row)
    return inv


def display_block(win, block, origin=(0,0), bw=False):
    """
    Displays an 8x8 image scaled up.
    :param win: the window from graphics.py to draw into
    :param block: the 8x8 array either as pixel intensity 0 -255 or bw as 0|1
    :param origin: where the top left corner of the block is drawn
    :param bw: True = black and white image stored as 0 = white, 1 = black
    :return:
    """
    scale = 8

    for x, row in enumerate(block):
        for y, pixel in enumerate(row):
            rect = Rectangle(Point(x*scale + origin[0], y*scale + origin[1]),
                             Point((x+1)*scale + origin[0], (y+1)*scale + origin[1]))
            if bw:
                rect.setFill(color_rgb(255*(1-pixel), 255*(1-pixel),255*(1-pixel)))
            else:
                rect.setFill(color_rgb(pixel, pixel, pixel))
            rect.setWidth(0)
            rect.draw(win)
    return

def xor_block(block1, block2):
    for x in range(8):
        for y in range(8):
            block1[x][y] = block1[x][y] ^ block2[x][y]
    return block1

def flip_it(block, x, y):
    """
    Inverts pixels at the given location and at the neighboring pixels
    :param block: 8x8 matrix of LED states: 1 or 0
    :param x: x coordinate of center position to flip
    :param y:
    :return: block with pixels updated
    """

    return block

"""
bases = []
for u in range(8):
    bases_row = []
    for v in range(8):
        basis = []
        for x in range(8):
            row = []
            for y in range(8):
                if x == u and y == v:
                    row.append(1023)
                else:
                    row.append(0)
            basis.append(row)
        inv = center_on_zero(inverse_dct(basis), True)
        # display_block(win, inv, (u * 75, v * 75))
        bases_row.append(inv)
    bases.append(bases_row)

win2 = GraphWin("DCT-BW", 600, 600)
for u in range(8):
    for v in range(8):
        for x in range(8):
            for y in range(8):
                if bases[u][v][x][y] > 127:
                    bases[u][v][x][y] = 0
                else:
                    bases[u][v][x][y] = 1
        display_block(win2, bases[u][v], (u * 68, v * 68), True)
win = GraphWin("DCT", 600, 600)
for u in range(8):
    for v in range(8):
        xored = xor_block(bases[randint(0,4)][randint(0,4)], bases[randint(0,4)][randint(0,4)])
        xored = xor_block(xored, bases[randint(0,4)][randint(0,4)])
        xored = xor_block(xored, bases[randint(0,4)][randint(0,4)])
#        xored = xor_block(xored, bases[randint(0,4)][randint(0,4)])
        display_block(win, xored, (u * 75, v * 75), True)

win.getMouse()
win.close()
win2.close()
"""
