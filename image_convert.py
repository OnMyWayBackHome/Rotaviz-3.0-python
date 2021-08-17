# Reads an image into an array for processing

import cv2
import sys
from math import degrees, atan2, sqrt, pi
from update_list_to_arduino import *
from operator import itemgetter #this allows for sorting lists based on sublist elements

image_size = 256 #pixel dimensions of the (square) image
number_of_leds = 32
number_of_updates = 72
bmp = "emma-logo-257.bmp"

def rc_to_xy(r, c, image_size):
   y  = - (r - image_size // 2)
   x = c - image_size // 2
   return (x,y)

def pixel_distance(xy_coords):
   distance = sqrt(xy_coords[0]**2 + xy_coords[1]**2)
   return distance

def led_number(number_of_leds, image_size, distance):
    number = round((distance / (image_size // 2)) * number_of_leds, 0)
    if number > number_of_leds:
        number = -1
    return int(number)

def pixel_angle(xy_coords):
    radiansx = (2*pi - atan2(xy_coords[1], xy_coords[0])) % (2*pi)
    return radiansx

def radians_per_update(number_of_updates):
    radians = 2 * pi / number_of_updates
    return radians

def update_number(radiansx, radians_per_update):
    update = radiansx // radians_per_update
    return int(update)

#Read the image from the file into an array (a list of lists).
#The first list is the color values of the first row, the second list is the 2nd row, etc. Note 255 is white, 0 is black
img = cv2.imread(bmp, 0)
if img is None:
    print("Image not loaded correctly. Check the file name. ")
    sys.exit() #Stop the program if the image wasn't read properly.
"""
# Print out the image as 0s and 1s
for r in range(image_size):
    for c in range(image_size):
        if img[r][c] == 0:
            pixel_state = 1
        else:
            pixel_state = 0
        print(pixel_state, end=' ')
    print('')
"""
# Convert each (row, column) in the image to an [update_number, led_number, pixel_state] list
updates_raw = []
for r in range(image_size):
    for c in range(image_size):
        xy_coords = rc_to_xy(r, c, image_size)
        rads = radians_per_update(number_of_updates)
        if img[r][c] == 0:
            pixel_state = 1  #pixel is on
        else:
            pixel_state = 0  #pixel is off
        #print(update_number(pixel_angle(xy_coords), rads), led_number(number_of_leds, image_size, pixel_distance(xy_coords)), pixel_state)
        led_numberx = led_number(number_of_leds, image_size, pixel_distance(xy_coords))
# Sarah,
# The program looks like it's calculating update_number and led_number correctly! Yay. On to the final step...
# Change the program so that it doesn't just print these values, but it appends them to a list of lists that I called updates_raw[].
# Each list in the list of lists will be [update_number, led_number, pixel_state] where pixel_state is 0/1 for on/off
# Don't forget to skip over (and not save to the list) any pixel that has an led_number of < 1.
# Then you will need to
# 1) make a loop inside a loop to go through all updates and led numbers (for u in range(number_of_updates): ...)
# For each update and led, search inside updates_raw and average all the pixel_states of the matching elements to see if the average is >= .5.
# For example, there might be three pixels in updates_raw that have the same update_number and led_number:
# [11, 7, 1], [11, 7, 0], [11, 7, 1] since 2 out of the 3 pixels are on, the pixel should be on for update 11, led 7.
# 2) Write these results to a final list of lists that has [update_number, led_number, led_state]
        if led_numberx > 0:
            updates_raw.append([update_number(pixel_angle(xy_coords), rads), led_numberx, pixel_state])


updates = []
for up in range(number_of_updates):
    for led in range(1,number_of_leds+1):
        count = 0
        sum = 0
        for update in updates_raw:
            if update[0] == up and update[1]==led:
                count += 1
                sum += update[2]
        if count == 0:
            status == 0
        if count != 0 and sum/count >= 0.5:
                status = 1
        else:
            status = 0

        updates.append([up, led, status])
#print(updates)
led_longs = update_list_to_longs(updates, number_of_updates, number_of_leds)
visualize_image(led_longs, number_of_leds, number_of_updates)
led_longs_to_arduino(led_longs)






