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
            content = content.replace("res://addons", themdir)
            outfile = open(outpath, 'w')
            outfile.write(content)
            outfile.flush()


def install(path):
    for theme in meta["themes"]:
        print("Installing theme {} to {}".format(theme['name'], path))
        if not os.path.isdir(path):
            os.makedirs(path)
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
            defaultdir = os.path.join(os.path.expanduser("~"), "AppData/Roaming/Godot/theme").replace("\\", "/")
        if defaultdir:
            install(defaultdir)
        else:
            print("Error: Unknown OS detected: {}.".format(osname))
    else:
        path = sys.argv[1]
        if os.path.isdir(path):
            install(path.replace("\\", "/"))
        else:
            print("Error: Directoy {} not found.".format(path))
