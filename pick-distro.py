#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pick-distro.py
#
#  Copyright 2020 Thomas Castleman <contact@draugeros.org>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
from __future__ import print_function
from random import randint
from sys import argv, stderr, version_info
from os import path

argc = len(argv)
VERSION = "0.0.3"
HELP = "\tPass nothing to provide a list of distros to prompts on screen.\n\n\t-h,--help\tPrint this help dialog\n\t--txt\t\tProvide a path to txt file with a list of distros to choose from. One distro per line.\n\t-v,--version\tPrint current version"

# Make it easier for us to print to stderr
def eprint(*args, **kwargs):
	print(*args, file=stderr, **kwargs)

if (version_info[0] == 2):
	eprint("Please run pick-distro.py with Python 3 as Python 2 is End-of-Life.")
	exit(2)

if (argc >= 2):
	if ((argv[1] == "--help") or (argv[1] == "-h")):
		print(HELP)
		exit(0)
	elif ((argv[1] == "-v") or (argv[1] == "--version")):
		print(VERSION)
		exit(0)
	elif (argv[1] == "--txt"):
		if ((argc >= 3) and (path.exists(argv[2]))):
			if (path.isfile(argv[2])):
				try:
					extension = (argv[2].split("."))[1]
				except:
					eprint("%s is not a *.txt file." % (argv[2]))
					exit(1)
				if ("txt" == extension):
					print("Reading %s. . . " % (argv[2]))
					with open(argv[2]) as dist_file:
						dists = dist_file.read()
					print("Parsing %s . . ." % (argv[2]))
					dists = dists.split("\n")
					dists = [x for x in dists if x != ""]
					print("Randomly picking a distro . . .")
					choice = randint(0,len(dists) - 1)
					print("This time the distro is: %s !" % (dists[choice]))
					exit(0)
				else:
					eprint("%s is not a *.txt file." % (argv[2]))
					exit(1)
			else:
				eprint("%s exists but is not a *.txt file." % (argv[2]))
				exit(1)
		else:
			eprint("File not provided or does not exist.")
			exit(1)
	else:
		eprint("Input not recognized.\n\n%s" % (HELP))
		exit(2)
else:
	dists = []
	while True:
		INPUT = input("Input Distro name (or 'continue' to randomly pick one, 'exit' to exit): ")
		if ((INPUT.lower() == "continue") or (INPUT.lower() == "cont")):
			if (len(dists) == 0):
				eprint("Nothing has been input. Please input a distro name before continuing.")
				continue
			dists = [x for x in dists if x != ""]
			print("Randomly picking a distro . . .")
			choice = randint(0,len(dists) - 1)
			print("This time the distro is: %s !" % (dists[choice]))
			exit(0)
		elif ((INPUT.lower() == "exit") or (INPUT.lower() == "break") or (INPUT.lower() == "cancel")):
			exit(0)
		else:
			dists.append(INPUT)
