# Automated Dune (2019) leaders
This is a little tool I developed to speed up the creation of the leader tokens for
homebrew factions for the Dune boardgame (2019 edition).

## Requirements

* Python 3
* LuaLaTex (with packages `geometry`, `fontspec`, `inputenc`, `xcolor`, `tikz`,
  `tikzpagenodes`, `graphicx`, `babel`, `contour`)
* Trebuchet MS and OPTI Copperplate (fonts)
* imagemagick

## How to use

You will need to create two folders in the same directory as `leader.tex`: `source` and
`images`.

`images` will be the folder where the end results will appear.
`source` will contain all the folders with assets and the key files to be compiled.

In order to use the tool, inside `source` create a new directory that will contain all
your assets for the leaders and faction. The name must be `Faction-R,G,B` where `R,G,B`
are the three components of the color of the leader disk.
Inside this folder, put all your assets:
* leader's files need to be named `Name-Strength` where `Strength` can be both a number
  or a letter
* faction's icon needs to be name `Faction-icon` where `icon` is the only important part
  (it is suggested to use `.png` files for the faction icon to aid with the transparency)

Open a terminal in the root folder of the project and run `python3 make_cards.py`, this
will create all the `.tex` files inside the `source/` folders that will later be
compiled. When that is done, run `./create_leaders.sh` and when the script ends, you
will find your assets in `images/Faction-R,G,B`.
