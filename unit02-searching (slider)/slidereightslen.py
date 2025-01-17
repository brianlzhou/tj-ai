import sys; args = sys.argv[1:]
import time; startTime = time.time()

str = '123_45678'
size = 3

lookup = {}

def getNeighbors(s):
    n=[]; i = s.find('_')
    if i in lookup:
        for p in lookup[i]:
            n.append(swap(s,i,p))
    else:
        temp = []
        if i % size < size-1: 
            n.append(swap(s, i, i+1))
            temp.append(i+1)
        if i % size > 0: 
            n.append(swap(s, i-1, i))
            temp.append(i-1)
        if i >= size: 
            n.append(swap(s, i-size, i))
            temp.append(i-size)
        if i < size **2 - size: 
            n.append(swap(s, i, i+size))
            temp.append(i+size)
        lookup[i] = temp
    return n

def swap(s, l, r):
    st = [*s]
    temp = st[l]
    st[l] = st[r]
    st[r] = temp
    return ''.join(st)

seenPuzzles = []
startingPuzzle = "1234_5678"
parseMe = [startingPuzzle]
seenPuzzles = []
levels = {0:[startingPuzzle]}

while parseMe:
    currLevel = len(levels)
    levels[currLevel] = []
    neighbors = []
    for pz in levels[currLevel-1]:
        neighs = getNeighbors(pz)
        for n in neighs:
            if n not in seenPuzzles:
                parseMe.append(n)
                seenPuzzles.append(n)
                levels[currLevel].append(n)
    print(f"level: {currLevel}, numofn: {len(levels[currLevel])}")