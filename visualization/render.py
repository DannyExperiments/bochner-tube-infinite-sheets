'''Render the demonstration GIF with Pillow.'''
from math import atan, atan2, cos, pi, sin
from pathlib import Path
import json
import re
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
WIDTH, HEIGHT = 680, 428
BACKGROUND, AQUA, GOLD, BLUE = '#162945', '#76e4d5', '#f3bf78', '#7792af'
FONT = ImageFont.load_default(size=20)
SMALL = ImageFont.load_default(size=16)

TITLE = 'One projection, infinitely many lifts'
SUBTITLE = 'A complete turn changes the logarithm by 2 pi i'
BASE = [(cos(t*pi/60), sin(t*pi/60), -1.26) for t in range(121)]


def lift(t):
    phase = t + atan2(-.1*sin(t), 2+.1*cos(t))
    return cos(t), sin(t), .7*(phase/(2*pi)-1.5)


PATH = [lift(k*pi/60) for k in range(361)]
POINTS = [lift(pi/12+k*2*pi) for k in range(3)]
FLOOR = [(POINTS[0][0], POINTS[0][1], -1.26)]
LINES = [(BASE, BLUE, 2), (FLOOR+POINTS, GOLD, 2), (PATH, AQUA, 4)]
DOTS = FLOOR+POINTS


def frame(azimuth):
    image = Image.new('RGB', (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(image)
    draw.text((21, 16), TITLE, font=FONT, fill='#e9f2fc')
    draw.text((21, HEIGHT-31), SUBTITLE, font=SMALL, fill='#e9f2fc')

    def project(point):
        x, y, z = point
        sx = cos(azimuth)*x - sin(azimuth)*y
        depth = sin(azimuth)*x + cos(azimuth)*y
        scale = HEIGHT*.245/(1+depth*.15)
        return WIDTH/2 + scale*sx, HEIGHT/2 - scale*(.87*z+.48*depth)

    for points, color, weight in LINES:
        draw.line([project(point) for point in points], fill=color, width=weight)
    for point in DOTS:
        x, y = project(point)
        draw.ellipse((x-5, y-5, x+5, y+5), fill=GOLD)
    return image


def main():
    frames = [frame(k*pi/24) for k in range(48)]
    frames[0].save(ROOT/'construction.gif', save_all=True, append_images=frames[1:],
                   duration=85, loop=0, optimize=True)


if __name__ == '__main__':
    main()
