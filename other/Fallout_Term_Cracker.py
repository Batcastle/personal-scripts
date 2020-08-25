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

def __find_largest__(array):
    largest = array[0]
    index = 0
    current_index = 0
    for each in array:
        if each == array[0]:
            current_index += 1
            continue
        elif largest < each:
            largest = each
            index = current_index
        current_index += 1
    return (largest, index)

def make_suggestion(passwords):
    scores = []
    current_score = 0
    for each in passwords:
        for each1 in passwords:
            if each == each1:
                continue
            elif each[0] == each1[0]:
                current_score += 1
            if each[-1] == each1[-1]:
                current_score += 1
        scores.append(current_score)
        current_score = 0
    best_chance = __find_largest__(scores)
    return (passwords[best_chance[1]], best_chance[0])

R = "\033[0;31m"
G = "\033[0;32m"
Y = "\033[1;33m"
BOLD = "\033[1m"
RESET = "\033[0m"
PASSWORDS = []
MODE = input("Select Mode: 1: JSON, 2: CLI Input: ")
if MODE.lower() in ("1", 1, "json"):
    FILENAME = input("Filename containing passwords: ")
    with open(FILENAME, "r") as file_obj:
        PASSWORDS = json.load(file_obj)
elif MODE.lower() in ("2", 2, "cli", "cli input"):
    INPUT = None
    while INPUT not in ("->", ">"):
        INPUT = input("Enter possible password, press enter to enter next password, 'X' or 'q' to exit, '->' to break password: ")
        INPUT = INPUT.lower()
        if INPUT in ("x", "q"):
            print("Exiting . . .")
            exit(0)
        PASSWORDS.append(INPUT)
if PASSWORDS[-1] in ("->", ">"):
    del PASSWORDS[-1]
print(Y + "compensating for capitalization . . ." + RESET)
for each in range(len(PASSWORDS)):
    PASSWORDS[each] = PASSWORDS[each].lower()
while True:
    if len(PASSWORDS) == 1:
        print("Most likely password: " + G + BOLD + PASSWORDS[0] + RESET)
        exit(0)
    elif len(PASSWORDS) == 0:
        print(R + BOLD + "ERROR: " + RESET + "No more possible passwords.")
        exit(1)
    suggest = make_suggestion(PASSWORDS)
    print("My current suggestion is: %s\nConfidence score: %s" % (suggest[0],
                                                                  suggest[1]))
    for each in range(len(PASSWORDS)):
        print("Password number " + str(each) + " :  " + PASSWORDS[each])
    TRYED = input("Tried password number: ")
    if TRYED.lower() in ("success", "exit", "quit", "done", "bye", "q", "x"):
        print("Exiting . . .")
        exit(0)
    TRYED = int(TRYED)
    DELETE = PASSWORDS[TRYED]
    LIKENESS = input("Likeness: ")
    if LIKENESS.lower() in ("success", "exit", "quit", "done",
                            "bye", "q", "x"):
        exit(0)
    else:
        try:
            LIKENESS = int(LIKENESS)
        except ValueError:
            print("ERROR: Not a recognized input. Please try again...")
            print("Hint: To exit, try entering 'exit' or 'quit'.")
            continue
    for each in range(len(PASSWORDS) - 1, -1, -1):
        if each == TRYED:
            continue
        for each1 in range(len(PASSWORDS[each])):
            if ((PASSWORDS[each][each1] == DELETE[each1]) and (LIKENESS == 0)):
                del PASSWORDS[each]
                break
            elif ((PASSWORDS[each][each1] == DELETE[each1]) and (LIKENESS > 0)):
                break
            elif ((PASSWORDS[each][each1] != DELETE[each1]) and (LIKENESS > 0) and ((each1 + 1) == len(PASSWORDS[each]))):
                del PASSWORDS[each]
                break
    del PASSWORDS[PASSWORDS.index(DELETE)]
