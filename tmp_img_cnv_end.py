        if led_number(number_of_leds, image_size, pixel_distance(xy_coords)) > 0:
            updates_raw.append([update_number(pixel_angle(xy_coords), rads), led_number(number_of_leds, image_size, pixel_distance(xy_coords)), pixel_state ])


updates = []
for update in range(number_of_updates):
    for led in range(number_of_leds):
        # Find the average value of the pixels for each update/led combo
        count = 0
        pixel_sum = 0
        for u in updates_raw:
            if u[0] == update and u[1] == led + 1:
                count += 1
                pixel_sum += u[2]
        if count > 0:
            pixel_state = round(pixel_sum / count)
        else:
            pixel_state = 0
        updates.append([update, led + 1, pixel_state])
print(updates)
