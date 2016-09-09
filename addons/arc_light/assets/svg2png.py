#!/usr/bin/env python

import rsvg
from xml.dom import minidom
import cairo
import os
import re
import fnmatch


def globPath(path, pattern):
    result = []
    for root, subdirs, files in os.walk(path):
        for filename in files:
            if fnmatch.fnmatch(filename, pattern):
                result.append(os.path.join(root, filename))
    return result


# convert svg file to png with scale
def svg2png(svg_file, output_file, scale=1):
    # Get the svg files content
    svg_data = open(svg_file).read()

    # Get the width / height inside of the SVG
    doc = minidom.parseString(svg_data)
    width = [path.getAttribute('width') for path in doc.getElementsByTagName('svg')][0]
    height = [path.getAttribute('height') for path in doc.getElementsByTagName('svg')][0]
    width = int(round(float(re.compile('(\d+\.*\d*)\w*').findall(width)[0])))
    height = int(round(float(re.compile('(\d+\.*\d*)\w*').findall(height)[0])))
    doc.unlink()

    # Create the png
    img = cairo.ImageSurface(
        cairo.FORMAT_ARGB32, width * scale, height * scale)
    ctx = cairo.Context(img)
    ctx.scale(scale, scale)
    handler = rsvg.Handle(None, str(svg_data))
    handler.render_cairo(ctx)
    img.write_to_png(output_file)
    print("{} ==> {}".format(svg_file, output_file))


dstdir = "icons"
if not os.path.isdir(dstdir):
    os.makedirs(dstdir)

for p in globPath('godot-design/assets/icons/svg', "**.svg"):
    if p.endswith('.svg'):
        dstfile = os.path.join(dstdir, os.path.basename(p))
        dstfile = dstfile.replace('.svg', '.png')
        if not os.path.isdir(os.path.dirname(dstfile)):
            os.makedirs(os.path.dirname(dstfile))
        svg2png(p, dstfile, 1)
        hidpiname = os.path.basename(dstfile)[: -len('.png')] + "@2x.png"
        dstfile = os.path.relpath(os.path.join(dstfile, "..", hidpiname))
        svg2png(p, dstfile, 2)
