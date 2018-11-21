"""
The idea is to eat the apple (tiny light in the center) with 
the worm (britest light moving as user rotates the Microbit).
Once you manage to place yourself on the apple, you win!
"""

import microbit

# Initial coordinates
x = 2
y = 2
delta_x = 0
delta_y = 0
counter = 0
finished = False

# Smiley image
smiley = (
    "00000:"
    "09090:"
    "00000:"
    "90009:"
    "09990"
)

# Main loop
while not finished:
    # At least one iteration is required for winning
    counter += 1
    
    # Clear display each time
    microbit.display.clear()
    
    # Show the apple
    microbit.display.set_pixel(2, 2, 4)
    
    # Get x and y coordinates
    _x = microbit.accelerometer.get_x()
    _y = microbit.accelerometer.get_y()
    
    # Detect x changes.
    # If x is aiming to be positive
    if _x > 1:
        delta_x = 1
    # If x is aiming to be negative
    elif _x < -1:
        delta_x = -1
    else:
        delta_x = 0
    
    # Detect y changes
    # If y is aiming to be positive
    if _y > 1:
        delta_y = 1
    # If y is aiming to be negative
    elif _y < -1:
        delta_y = -1
    else:
        delta_y = 0
    
    # Reflecting changes on the board
    x += delta_x
    y += delta_y
    
    # Normalising the x and y values before rendering
    if x < 0:
        x = 0
    elif x > 4:
        x = 4
    if y < 0:
        y = 0
    elif y > 4:
        y = 4

    # Rendering the pixel
    microbit.display.set_pixel(x, y, 9)
    microbit.sleep(100)
    
    # Detect if user won
    if counter > 0 and x == 2 and y == 2:
        finished = True
        microbit.display.show(microbit.Image(smiley), delay=0, wait=False, loop=False, clear=False)