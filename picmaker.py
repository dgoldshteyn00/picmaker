import random


def draw():
    f = open("image.ppm", "w")
    f.write("P3\n500 500\n255\n")

    fire = 0
    for i in range(100):
        row = ""
        for j in range(100):
            check = random.random()
            # to burn or not to burn
            if check < fire:
                # semi-random embers
                red = random.randint(175, 255)
                green = random.randint(0, 50)
                blue = random.randint(0, 50)
            else:
                # non-random background
                red = 51
                green = 25
                blue = 0
            row += (str(red) + " " + str(green) + " " + str(blue) + " ") * 5
        f.write((row + "\n") * 5)
        fire += 0.013
    f.close()


draw()
