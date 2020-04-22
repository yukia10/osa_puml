# -*- coding: utf-8 -*-
"""
conv_icon.py - Script to convert icon images

## Usage
$ mkdir ./osa_puml
$ cd ./osa_puml
$ wget http://www.opensecurityarchitecture.org/downloads/13_05_osa_icons_png.zip
$ mkdir ./icons
$ cd ./icons
$ unzip ../13_05_osa_icons_png.zip
$ python3 ../conv_icon.py
$ cd ..
$ wget https://github.com/milo-minderbinder/AWS-PlantUML/archive/18.2.22.tar.gz -O AWS-PlantUML-18.2.22.tar.gz
$ tar zxf AWS-PlantUML-18.2.22.tar.gz
$ cd AWS-PlantUML-18.2.22
$ python3 puml.py -c ./puml.ini ../icons
$ mkdir ../osa
$ cp dist/osa/*/*.puml ../osa
"""

import glob
import re
import os
from PIL import Image

def im_conv(file):
    im = Image.open(file)
    bg = Image.new('RGBA', im.size, (255, 255, 255))
    im = Image.alpha_composite(bg, im).convert("L")
    _min, _max = im.getextrema()
    lut = [round(255 * (k - _min) / (_max - _min)) for k in range(256)]
    im = im.point(lut)
    _gamma = 1.2
    lut = [round(255 * (k / 255)**(1.0 / _gamma)) for k in range(256)]
    im = im.point(lut)
    im.convert("RGB").save(file)

L = glob.glob("*.png")
L.sort()

for file in L:
    im_conv(file)

TRANSLATIONS = (
    ('arrow_green_', 'arrow_'),
    ('arrow_yellow_', 'arrow_'),
    ('desktop_imac', 'iMac'),
    ('-generic', ''),
    ('user_blue_', 'user_'),
    ('user_green_', 'user_'),
    ('user_large_group', 'users_large_group'),
    ('users_blue_green', 'users_group'),
)

R = [re.sub('osa_', '', s) for s in L]
for pattern, repl in TRANSLATIONS:
    R = [re.sub(pattern, repl, s) for s in R]
R = [re.sub('_', '-', s) for s in R]
R = ["osa_" + s for s in R]

for src, dst in zip(L, R):
    os.rename(src, dst)
