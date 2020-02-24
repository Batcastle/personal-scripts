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
# Basic set up
from __future__ import print_function
from random import randint
from sys import argv, stderr, version_info
from os import path


# get length of argument array
argc = len(argv)
# set version
VERSION = "0.0.5"
# set help dialog
HELP = "\tPass nothing to provide a list of distros to prompts on screen.\n\n\t-h,--help\tPrint this help dialog\n\t--txt\t\tProvide a path to txt file with a list of distros to choose from. One distro per line.\n\t-v,--version\tPrint current version"

# Make it easier for us to print to stderr
def eprint(*args, **kwargs):
	print(*args, file=stderr, **kwargs)

# save some lines of code with a function to do the chosing
def pick_distro(dists):
	dists = [x for x in dists if x != ""]
	print("Randomly picking a distro . . .")
	choice = randint(0,len(dists) - 1)
	print("This time the distro is: %s !" % (dists[choice]))

# Now comes the actual processing . . .

# Make sure we did all this in Python 3, not Python 2
if (version_info[0] == 2):
	eprint("Please run pick-distro.py with Python 3 as Python 2 is End-of-Life.")
	exit(2)

# Check to see if we even HAVE any arguments
if (argc >= 2):
	# Help dialog
	if ((argv[1] == "--help") or (argv[1] == "-h")):
		print(HELP)
		exit(0)
	# Version output
	elif ((argv[1] == "-v") or (argv[1] == "--version")):
		print(VERSION)
		exit(0)
	# Read from plain text file
	elif (argv[1] == "--txt"):
		# Make sure the file actually exists
		if ((argc >= 3) and (path.exists(argv[2]))):
			# Make sure the file is actually a file
			if (path.isfile(argv[2])):
				# Check for a *.txt extension
				try:
					extension = (argv[2].split("."))[1]
				except:
					eprint("%s is not a *.txt file." % (argv[2]))
					exit(1)
				if ("txt" == extension):
					# Read the file
					print("Reading %s. . . " % (argv[2]))
					with open(argv[2]) as dist_file:
						dists = dist_file.read()
					# Split everything up so we have just the names of the distros
					print("Parsing %s . . ." % (argv[2]))
					dists = dists.split("\n")
					# Pick a distro
					pick_distro(dists)
					exit(0)
				else:
					# Not a *.txt file
					eprint("%s is not a *.txt file." % (argv[2]))
					exit(1)
			else:
				# It may exist but it isn't a *.txt file
				eprint("%s exists but is not a *.txt file." % (argv[2]))
				exit(1)
		else:
			# No file provided or the file does not exist
			eprint("File not provided or does not exist.")
			exit(1)
	else:
		# Invalid input
		eprint("Input not recognized.\n\n%s" % (HELP))
		exit(2)
else:
	# No input provided, take input in the form of prompts
	dists = []
	while True:
		# cyclicly ask the user for a distro until they say to continue
		INPUT = input("Input Distro name (or 'continue' to randomly pick one, 'exit' to exit): ")
		if ((INPUT.lower() == "continue") or (INPUT.lower() == "cont")):
			#pull all the empty strings out BEFORE checking length
			dists = [x for x in dists if x != ""]
			if (len(dists) == 0):
				# they put nothing in and went straight to continue. This would normally throw an error.
				# Stop that error and let them try again
				eprint("Nothing has been input. Please input a distro name before continuing.")
				continue
			# we good so pick a distro
			pick_distro(dists)
			exit(0)
			# Exit from the program
		elif ((INPUT.lower() == "exit") or (INPUT.lower() == "break") or (INPUT.lower() == "cancel")):
			exit(0)
		else:
			# Nothing else was provided so append what we assume is a distro name to the list of possible candidates
			dists.append(INPUT)
