#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  hex_to_decimal.py
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
from sys import argv

def __convert_hex__(hex_string):
  sum = 0
  equiv = {"A":10, "B":11, "C":12, "D":13,"E":14, "F":15}
  hex_string = hex_string.upper()
  rounds = 0
  for each in range(len(hex_string) - 1, -1, -1):
    try:
      value = int(hex_string[each])
    except ValueError:
      value = equiv[hex_string[each]]
    sum = sum + ((16 ** rounds) * value)
    rounds += 1
  return(sum)

def HEX_TO_RGB(hex_code, string=False):
    rgb = []
    output = []
    if hex_code[0] == "#":
        hex_code = hex_code[1:]
    if len(hex_code) not in (6, 8):
        return None
    rgb.append(hex_code[0:2])
    rgb.append(hex_code[2:4])
    rgb.append(hex_code[4:6])
    if len(hex_code) == 8:
        rgb.append(hex_code[6:8])
    for each in rgb:
        output.append(__convert_hex__(each))
    if not string:
        return(output)
    else:
        output = ", ".join([str(x) for x in output])
        return("rgb(%s)" % (output))

if __name__ == "__main__":
    if len(argv) < 2:
        print("\n" + HEX_TO_RGB(input("Hex code to convert to rgb(): "), string=True))
    else:
        print("\n" + HEX_TO_RGB(argv[1], string=True))
