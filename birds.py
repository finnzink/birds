import copy 

matchings = {"blueT": "blueH", "blueH": "blueT", 
    "reddT": "reddH", "reddH": "reddT", 
    "yellT": "yellH", "yellH": "yellT", 
    "multT": "multH", "multH": "multT"}

tiles = [{"north":"multT","east":"yellH","south":"reddH","west":"blueT"},
    {"north":"multH","east":"blueH","south":"reddT","west":"yellT"},
    {"north":"multH","east":"reddH","south":"blueH","west":"blueT"},
    {"north":"reddT","east":"blueH","south":"multT","west":"yellH"},
    {"north":"reddH","east":"yellH","south":"multH","west":"blueT"},
    {"north":"blueT","east":"multT","south":"reddT","west":"yellT"},
    {"north":"reddT","east":"yellH","south":"blueT","west":"multT"},
    {"north":"yellH","east":"yellT","south":"multT","west":"blueH"},
    {"north":"reddH","east":"blueH","south":"multT","west":"yellH"}]

def rotateLeft(tile):
    temp = copy.deepcopy(tile)
    temp["north"] = tile["east"]
    temp["east"] = tile["south"]
    temp["south"] = tile["west"]
    temp["west"] = tile["north"]
    return temp

def checkEdges(tilesUsed, i):
    # only need to check north and west 
    if (i > 2 and matchings[tilesUsed[i]["north"]] != tilesUsed[i-3]["south"]):
        return False
    if (i % 3 != 0 and matchings[tilesUsed[i]["west"]] != tilesUsed[i-1]["east"]):
        return False
    return True

def printSolution(tilesUsed):
    print("SOLUTION:")
    for i in range(0, 3):
        print("-------------------------------------------------")
        print("|     " + tilesUsed[3*i+0]["north"] + "     |     " + tilesUsed[3*i+1]["north"] + "     |     " + tilesUsed[3*i+2]["north"] + "     |")
        print("|" + tilesUsed[3*i+0]["west"] + "     " + tilesUsed[3*i+0]["east"] + "|" + tilesUsed[3*i+1]["west"] +"     "+ tilesUsed[3*i+1]["east"] + "|" + tilesUsed[3*i+2]["west"] +"     "+ tilesUsed[3*i+2]["east"] + "|")
        print("|     " + tilesUsed[3*i+0]["south"] + "     |     " + tilesUsed[3*i+1]["south"] + "     |     " + tilesUsed[3*i+2]["south"] + "     |")
    print("-------------------------------------------------")
    print("\n")

def recurse(posOfTiles, curr, tilesUsed):
    pos = copy.deepcopy(posOfTiles)
    for i in range(0, 9):
        if i not in tilesUsed:
            pos[curr] = tiles[i]
            used = copy.deepcopy(tilesUsed)
            used.append(i)
            for _ in range(0, 4):
                pos[curr] = rotateLeft(pos[curr])
                if checkEdges(pos, curr):
                    if curr > 7:
                        printSolution(pos)
                    else:
                        recurse(pos, curr + 1, used)


recurse({}, 0, [])
