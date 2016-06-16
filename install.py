#!/usr/bin/env python

import os
import sys
import json
import fnmatch
import shutil
import platform

cwd = os.getcwd()
meta = json.load(open(os.path.join(cwd, "theme.json")))



def globPath(path, pattern):
    result = []
    for root, subdirs, files in os.walk(path):
        for filename in files:
            if fnmatch.fnmatch(filename, pattern):
                result.append(os.path.join(root, filename))
    return result


def handleFile(inpath, outpath, themdir):
    parentdir = os.path.abspath(os.path.join(outpath, os.pardir))
    if not os.path.isdir(parentdir):
        os.makedirs(parentdir)
    if os.path.isfile(inpath):
        if not inpath.endswith(".tres"):
            shutil.copy(inpath, parentdir)
            return
        else:
            content = open(inpath).read()
            content = content.replace(
                "res://addons/themes", themdir, sys.maxint)
            outfile = open(outpath, 'w')
            outfile.write(content)
            outfile.flush()


def install(path):
    for theme in meta["themes"]:
        print("Installing theme %s to %s" % (theme['name'], path))
        for p in globPath(theme['dir'], "*"):
            op = os.path.abspath(os.path.join(
                path, theme["name"], os.path.relpath(p, theme['dir'])))
            handleFile(p, op, path)
    print("Done!")

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        osname = platform.system()
        defaultdir = None
        if osname == "Linux" or osname == "Darwin":
            defaultdir = os.path.join(os.path.expanduser("~"), ".godot/theme")
        elif osname == "Windows":
            defaultdir = "C://.godot/theme"
        if defaultdir:
            install(defaultdir)
        else:
            print("Error: Unknown OS detected: %s." % osname)
    else:
        path = sys.argv[1]
        if os.path.isdir(path):
            install(path)
        else:
            print("Error: Directoy %s not found." % path)
