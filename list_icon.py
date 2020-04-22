# -*- coding: utf-8 -*-
"""
list_icon.py - Script to produce an image of all icons

## Usage
$ python3 list_icon.py > icons.md
$ code icons.md ## Visual Studio Code
   Preview icons.md with Markdown Preview Enhanced
   Open in Browser (Firefox)
   Firefox Screenshots > Capture a full page > icons.png
$ mogrify -trim icons.png
$ mogrify -mattecolor "#FFF" -frame 16x16 icons.png
"""

import glob
import re
import os
import math

L = glob.glob("osa/*.puml")
L = [s for s in L if not re.match(r'.*-sprite.puml$', s)]
L.sort()

HEAD = """
```puml
skinparam defaultTextAlignment center

!$OSA = "./osa"
"""
print(HEAD)
L = [os.path.splitext(os.path.basename(s))[0] for s in L]
for file in L:
    print("!include $OSA/%s.puml" % os.path.basename(file))
for file in L:
    print('agent "%s\\n<$%s{scale=0.5}>" as %s' % (file, file, file))
n = math.ceil(math.sqrt(len(L)))
for t in [L[i::n] for i in range(n)]:
    for i in range(len(t) - 1):
        print("%s -[hidden]d-> %s" % (t[i], t[i + 1]))
print("```") # TAIL
