from PIL import Image, ImageDraw

MAX_ITER = 100
C = 3*10**8

def sequence(v):
    u = 0
    n = 0
    while abs(u) <= 2 and n < MAX_ITER:
        u = (v + u)/(1 + v*u/(C*C))
        n += 1
    return n

# Image size (pixels)
WIDTH = 600
HEIGHT = 400

# Plot window
RE_START = -0.5
RE_END = 0.5
IM_START = -0.5
IM_END = 0.5

im = Image.new('HSV', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)

for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        # Convert pixel coordinate to complex number
        v = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                    IM_START + (y / HEIGHT) * (IM_END - IM_START))
        # Compute the number of iterations
        m = sequence(v)
        # The color depends on the number of iterations
        hue = int(255 * m / MAX_ITER)
        saturation = 255
        value = 255 if m < MAX_ITER else 0
        # Plot the point
        draw.point([x, y], (hue, saturation, value))

im.convert('RGB').save('train_fractal.png', 'PNG')
