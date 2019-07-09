# RA Shortcut Creator
# Made by lilbud
# Version 2.0

import os, sys

# REPLACE THESE LINES WITH PATHS TO YOUR FOLDERS v

RAFOLDER = "D:\Emulation\Other Files\RetroArch"
CORES_DIR = os.path.join(RAFOLDER, "Cores")
RA_LOCATION = os.path.join(RAFOLDER, "retroarch.exe")
ROM_PATH = "D:\\Emulation\\Nintendo\\Super Nintendo Entertainment System\\ROMs\\"

# REPLACE THESE LINES WITH PATHS TO YOUR FOLDERS ^

RA = "\"" + RA_LOCATION + "\""

cores = os.listdir(CORES_DIR)
games = os.listdir(ROM_PATH)
hiddenext = [".srm", ".sav", ".bat", ".ups", ".bsz", ".txt", ".cht"]
hidden = []

for item in games:
    if item.endswith(tuple(hiddenext)):
        hidden.append(item)
        continue

global romlist

romlist = [i for i in games if i not in hidden]

def corechoice():
    x = 0
    for item in cores:
        x = x + 1
        print(x, "- " + item)

    global new_core_string, finalcorepath

    corechoice = (int(input("Which Core Would You Like to Use?: ")))
    make_string = (str(cores[corechoice - 1:corechoice]))
    new_core_string = make_string.replace("'",'').replace("[","").replace("]", "")
    corepath = os.path.join(CORES_DIR, new_core_string)
    finalcorepath = "\"" + corepath + "\""

def romlisting():
    x = 0
    for item in romlist:
        x = x + 1
        print(x, "- " + item)
    
def romchoice():
    global new_rom_string, finalrompath
    gamechoice = (int(input("Which Game Would You Like to Choose? (or 99 for all games): ")))
    if gamechoice == "99":
        batchcreate()
    make_string = (str(romlist[gamechoice - 1:gamechoice]))
    new_rom_string = make_string.replace("'", "").replace("[", "").replace("]", "").replace('"', "")
    rompath = os.path.join(ROM_PATH, new_rom_string)
    finalrompath = " " + "\"" + rompath + "\""

def filewrite():
    file = open(new_rom_string + ".bat","w+")
    file.write(RA)
    file.write(" -L ")
    file.write(finalcorepath)
    file.write(finalrompath)

def rerun():
    romchoice()
    filewrite()

def check():
    anotherone = input("Would You Like to Make Another Shortcut?: ")
    if anotherone == "yes":
        rerun()
        check()
    if anotherone == "no":
        exit

def main():
    corechoice()
    romlisting()
    romchoice()
    filewrite()
    check()

main()


        




