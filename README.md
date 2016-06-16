# Godot UI theme

UI themes for godot applications.

## For editor

Themes can be applied to Godot editor after install.

* Run `python install.py` to install the themes.
* Select the theme path end with `.tres` under your install directory in godot editor with `Settings/Global/Custom Theme`.

You can pass a param to run `install.py` to set install directory.

### Default install directory

It should put into the `theme` folder under your `.godot` folder.

I don't know the where the `.godot` folder located on Windows platform, so I just set it to `C://.godot/theme` you can pull a PR to fix it in `install.py` and remove this message

## For your projects

Just copy the `addons` folder into you project folder.

## For designers(To create your own theme)

* Create your theme under the addons folder
* All resources created with godot editor should saved to '.tres'
* Fill the `theme.json`
