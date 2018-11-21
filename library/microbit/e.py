import microbit

brightness_up = [i for i in range(0, 9)]
brightness_down = [i for i in reversed(brightness_up)][:-1]
brightness = brightness_up + brightness_down

# E
IMAGE = (
    "11110:"
    "10000:"
    "11100:"
    "10000:"
    "11110"
)

while True:
    for intensivity in brightness:
        image = IMAGE.replace("1", str(intensivity))
        microbit.display.show(microbit.Image(image), delay=0, wait=False, loop=False, clear=False)
        microbit.sleep(100)