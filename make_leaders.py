#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 Davide Cossu <cossu.dvd@gmail.com>
#
# Distributed under terms of the CC BY-NC license.

"""
    This utility program will create the necessary .tex files for the cards in the
    decks.

    Reads the contents of a file and parses them.
"""

import os

def main():
    
    directories = [x[1] for x in os.walk("./source/")][0]

    with open("leader.tex") as f:
        card_file_content = f.read().splitlines()

    for faction in directories:
        pieces = faction.split("-")
        fname = pieces[0]
        fcolor = pieces[1]
        icon = ""
        for leader in os.scandir("./source/"+faction):
            if "icon" in leader.name:
                icon = "./"+leader.name
        for leader in os.scandir("./source/"+faction):
            if not leader.name.endswith(".tex"):
                if not "icon" in leader.name:
                    chunks = leader.name.split("-")
                    name = chunks[0].replace(".png","").replace("_"," ")
                    strength = chunks[1].replace(".png","").replace(".jpg","")
                    art = "./"+leader.name

                    fo = open("./source/"+faction+"/"+name.replace(" ","_")+".tex","w+")
                
                    for line in card_file_content:
                        if "\\newcommand\\leaderName" in line:
                            line = line.replace("Leader-Name", name)
                        elif "\\newcommand\\leaderStrength" in line:
                            line = line.replace("1", strength)
                        elif "\\newcommand\\leaderArt" in line:
                            line = line.replace("example-image", art)
                        elif "\\newcommand\\factionArt" in line:
                            line = line.replace("example-image", icon)
                        elif "\\definecolor" in line:
                            line = line.replace("000,111,222", fcolor)

                        fo.write(line+"\n")

                    fo.close()


if __name__ == "__main__":
    main()

