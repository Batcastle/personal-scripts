Scripts in here are things I made for other people, or to have some fun.


pick-distro.py
---
`pick-distro.py` is used on [BDLL](https://bigdaddylinux.com/) to pick the new distro for the distro challenge every week.
Currently it supports a TUI and reading from a *.txt file.

I am thinking about adding support for reading *.csv files, and reading distro names as arguments. 

disk_bench.sh
---
`disk_bench.sh` is a disk benchmark tool I made for [Swivro](swivro.net). It's written in BASH so that it can run on both MacOS and Linux.

Fallout_Term_Cracker.py
---
This program is used to reduce the amount of time it takes to hack Fallout 4 terminals in game. It is not a game mod or hack. It run it seperatly from the game, manually tell it the password options, either on CLI or in a JSON file (hence the presence of `passwords.json`), then manually tell it what passwords you are guessing. It will narrow down the options for you. 

hex_to_rgb.py
---
This script will convert any HTML Hex code used for colors to an rgb() call in CSS. It can be used on CLI, or as part of a larger program by importing it like a Python library.