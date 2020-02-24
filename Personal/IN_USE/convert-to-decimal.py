#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  convert-to-decimal.py
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
#  Convert Decimal input to Binary
from sys import argv, stderr, version_info

#actual conversion algorithim
def convert_to_decimal(text,bit_size,standard = True):
	total = 0
	for each in range(0,len(text)):
		if (text[each] == "1"):
			#check for if we are using Two's Compliment or standard binary
			#assuming big endian
			if ((each == 0) and ( not standard)):
				total = total + (-1 * bit_size)
			else:
				total = total + bit_size
		bit_size = bit_size / 2
	return(total)

#figure out what the size of the left-most bit is
def find_bit_size(text):
	bit_size = 1
	for each in range(0,len(text)):
		if (each != 0):
			bit_size = bit_size * 2
	return(bit_size)

# Make it easier for us to print to stderr
def eprint(*args, **kwargs):
	print(*args, file=stderr, **kwargs)

if (version_info[0] == 2):
	eprint("Please run with Python 3 as Python 2 is End-of-Life.")
	exit(2)

argc = len(argv)
HELP = "-h,--help\t\tView this help dialog\n-v,--version\t\tPrint version\n-g,--gui\t\tUse GUI\n-t,--tui\t\tUse TUI"
VERSION = "0.0.2-alpha2"
if (argc <= 1):
	eprint("Nothing passed")
	print(HELP)
elif ((argv[1] == "-h") or (argv[1] == "--help")):
	print(HELP)
elif ((argv[1] == "-v") or (argv[1] == "--version")):
	print(VERSION)
elif ((argv[1] == "-t") or (argv[1] == "--tui")):
	while True:
		data = input("Binary to convert: ")
		method = input("Standard or Two's Compliment [S/T]: ")
		method = method.lower()
		if (method == "s"):
			print(round(convert_to_decimal(data,find_bit_size(data))))
		elif (method == "t"):
			print(round(convert_to_decimal(data,find_bit_size(data),False)))
		elif (method == "exit"):
			exit(0)
		else:
			eprint("Answer not understood")
			continue;
		answer = input("Would you like to go again? [y/N]: ")
		answer = answer.lower()
		if (answer == "n"):
			exit(0)
elif ((argv[1] == "-g") or (argv[1] == "--gui")):
	eprint("GUI not currently implemented. Please use the TUI.")
	exit(1)
else:
	eprint("Arguments not understood")
	print(HELP)
