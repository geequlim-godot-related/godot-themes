# Godot UI theme

Editor themes for Godot engine.

## For the editor

Themes can be choosen in the Godot editor after installation.

* Run `python install.py` to install the themes.
* Select the theme. To do so choose the file ending with `.tres` in the godot editor settings. You can find the coustom theme option in the editor settings: `Settings/Global/Custom Theme`.


### Default installation directory

The installation script should move the files into the `theme` folder inside your `.godot` folder.
If you have a windows machine it will be installed here: `AppData/Roaming/Godot`.

## For your own projects
(using the theme inside a your game)

Just copy the `addons` folder into your godot project folder.
You can select the theme for any UI element in your project. This element and all it's children now are going to use the custom theme.

## For designers
(To create your own theme)

* Create your theme inside the addons folder
* All the resources which are created with the godot editor should be saved to the '.tres' file
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
![](https://cdn.rawgit.com/Geequlim/depot/master/images/godot/arc_light_lowDPI1.png)

### Adobe themes

* These themes are inspired by Adobe Photoshop.
![](https://cdn.rawgit.com/Geequlim/depot/master/images/godot/adobe_light.png)
![](https://cdn.rawgit.com/Geequlim/depot/master/images/godot/adobe_normal.png)
![](https://cdn.rawgit.com/Geequlim/depot/master/images/godot/adobe_dark.png)
