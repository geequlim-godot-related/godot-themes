# Godot UI theme

UI themes for godot engine.

## For the editor

The themes can be applied to the Godot editor after installation.

* Run `python install.py` to install the themes.
* Select the theme path ending with `.tres` under your install directory in the godot editor with `Settings/Global/Custom Theme`.

You can pass a param to run `install.py` to set install directory.

### Default install directory

It should install it into the `theme` folder under your `.godot` folder.

I don't know the where the `.godot` folder is located on Windows platform, so I just set it to `C://.godot/theme` you can pull a PR to fix it in `install.py` and remove this message

## For your projects

Just copy the `addons` folder into your project folder.

## For designers(To create your own theme)

* Create your theme under the addons folder
* All resources created with godot editor should be saved to '.tres'
* Fill the `theme.json`


## Screenshots

### Arc Dark

* This theme is inspired by [horst3180's arc-theme](https://github.com/horst3180/arc-theme).
* Both LDPI and HiDPI are supported
![](https://cdn.rawgit.com/Geequlim/depot/master/images/godot/arc_dark_pm.png)
![](https://cdn.rawgit.com/Geequlim/depot/master/images/godot/arc_dark_LDPI.png)
![](https://cdn.rawgit.com/Geequlim/depot/master/images/godot/arc_dark_HiDPI.png)

### Arc Light
* This theme is inspired by [horst3180's arc-theme](https://github.com/horst3180/arc-theme).
* The theme is under development
![](https://cdn.rawgit.com/Geequlim/depot/master/images/godot/arc_light_HiDPI.png)
