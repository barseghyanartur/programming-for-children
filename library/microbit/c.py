import microbit

brightness_up = [i for i in range(0, 9)]
brightness_down = [i for i in reversed(brightness_up)][:-1]
brightness = brightness_up + brightness_down

# C
IMAGE = (
    "01110:"
    "10000:"
    "10000:"
    "10000:"
    "01110"
)

while True:
    for intensivity in brightness:
        image = IMAGE.replace("1", str(intensivity))
        microbit.display.show(microbit.Image(image), delay=0, wait=False, loop=False, clear=False)
        microbit.sleep(100)