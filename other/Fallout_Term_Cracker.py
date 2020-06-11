#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Fallout_Term_Cracker.py
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

import json

R = "\033[0;31m"
G = "\033[0;32m"
Y = "\033[1;33m"
NC = "\033[0m"
PASSWORDS = []
MODE = input("Select Mode: 1: JSON, 2: CLI Input: ")
if MODE.lower() in ("1", 1, "json"):
    FILENAME = input("Filename containing passwords: ")
    with open(FILENAME, "r") as file_obj:
        PASSWORDS = json.load(file_obj)
elif MODE.lower() in ("2", 2, "cli", "cli input"):
    INPUT = None
    while INPUT not in ("continue", "next", "proceede"):
        INPUT = input("Enter possible password, press enter to enter next password, 'exit' to exit, 'next' to break password: ")
        INPUT = INPUT.lower()
        if INPUT in ("success", "exit", "quit", "done", "bye"):
            print("Exiting . . .")
            exit(0)
        PASSWORDS.append(INPUT)
print(Y + "compensating for capitalization . . ." + NC)
for each in range(len(PASSWORDS)):
    PASSWORDS[each] = PASSWORDS[each].lower()
while True:
    if len(PASSWORDS) == 1:
        print(G + "Most likely password: " + PASSWORDS[0] + NC)
        exit(0)
    for each in range(len(PASSWORDS)):
        print("Password number " + str(each) + " :  " + PASSWORDS[each])
    TRYED = input("Tried password number: ")
    if TRYED.lower() in ("success", "exit", "quit", "done", "bye"):
        print("Exiting . . .")
        exit(0)
    TRYED = int(TRYED)
    DELETE = PASSWORDS[TRYED]
    LIKENESS = int(input("Likeness: "))
    for each in range(len(PASSWORDS) - 1, -1, -1):
        if each == TRYED:
            continue
        for each1 in range(len(PASSWORDS[each]) - 1, -1, -1):
            if ((PASSWORDS[each][each1] == PASSWORDS[TRYED][each1]) and (LIKENESS == 0)):
                del PASSWORDS[each]
                break
            elif ((PASSWORDS[each][each1] != PASSWORDS[TRYED][each1]) and (LIKENESS > 0) and ((each1 + 1) == len(PASSWORDS[each]))):
                del PASSWORDS[each]
                break
    del PASSWORDS[PASSWORDS.index(DELETE)]