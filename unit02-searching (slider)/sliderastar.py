import sys; args = sys.argv[1:]
import time; 
import math;
if args:
    with open(args[0]) as f:
        myL = [str.strip() for str in f]
else:
    with open('Eckel.txt') as f:
        myL = [str.strip() for str in f]
goal = myL[0]; 
size = 4

def astar(start, goal):
    if not isSolvable(start,goal): return 'X'
    if start==goal: return 'G'
    openSet=[[] for n in range (80)] # create a openSet tuple of (h, puzzle, previous, move, layer)
    openSet[(firstH:=h(start,goal))].append((firstH,start,'end','',0))
    closedSet = {}
    index = 79
    incremDict = {}

    #create character dictionary of the goal 
    for char in goal:
        incremDict[char] = ((charidx:=goal.index(char))//4,charidx%4) #dictionary of row and col

    while True:
        # find pz with lowest total estimate
        if openSet[index]:
            pz = openSet[index].pop()
        else:
            for i in range(80):
                if openSet[i]:
                    index = i
                    pz = openSet[i].pop()
                    break
        if pz[1] in closedSet: continue
        closedSet[pz[1]] = pz[2]

        # if we have reached the end
        if pz[1] == goal:
            path = ''
            while pz[2] != 'end': 
                path = path + pz[3]
                pz = pz[2]
            return path[::-1]

        # creating neighbors
        n=[]; i = pz[1].index('_')
        if i in lookup:
            for p in lookup[i]:
                n.append((swap(pz[1],i,p[0]), p[1]))
        else:
            temp = []
            if i % size < size-1: 
                n.append((swap(pz[1], i, i+1), 'R'))
                temp.append((i+1, 'R'))
            if i % size > 0: 
                n.append((swap(pz[1], i-1, i), 'L'))
                temp.append((i-1, 'L'))
            if i >= size: 
                n.append((swap(pz[1], i-size, i), 'U'))
                temp.append((i-size, 'U'))
            if i < size **2 - size: 
                n.append((swap(pz[1], i, i+size), 'D'))
                temp.append((i+size, 'D'))
            lookup[i] = temp

        # adding neighbors to the next run-through
        for nbr in n:
            if nbr[0] not in closedSet:
                f = pz[0]+1+hoptimal(nbr[0],pz[1],goal,incremDict) #first add the prior, then 1 for the layer, then the increment
                openSet[f].append((f,nbr[0],pz,nbr[1],pz[4]+1))
                if f < index:
                    index = f
            

lookup = {}

def neighbors(s):
    n=[]; i = s.find('_')
    if i in lookup:
        for p in lookup[i]:
            n.append((swap(s,i,p[0]), p[1]))
    else:
        temp = []
        if i % size < size-1: 
            n.append((swap(s, i, i+1), 'R'))
            temp.append((i+1, 'R'))
        if i % size > 0: 
            n.append((swap(s, i-1, i), 'L'))
            temp.append((i-1, 'L'))
        if i >= size: 
            n.append((swap(s, i-size, i), 'U'))
            temp.append((i-size, 'U'))
        if i < size **2 - size: 
            n.append((swap(s, i, i+size), 'D'))
            temp.append((i+size, 'D'))
        lookup[i] = temp
    return n

def swap(s, l, r):
    st = [*s]
    temp = st[l]
    st[l] = st[r]
    st[r] = temp
    return ''.join(st)

inversionLookup = {}
def inversionct(str):
    if str in inversionLookup:
        return inversionLookup[str]
    else:
        count = 0; 
        for left in range(size**2-1):
            for right in range(left+1, size**2):
                if str[left] =='_' or str[right] == '_': continue
                if str[left] > str[right]: count = count + 1
        inversionLookup[str] = count
        return count

solvableLookup = {}
def isSolvable(pz,goal):
    if pz in solvableLookup:
        return solvableLookup[pz]
    else:
        invs = inversionct(pz); invg = inversionct(goal)
        if size % 2: 
            return invs % 2 == invg % 2 # if odd
        else: 
            solvableLookup[pz] = (returner := ((pz.index('_')//size) + invs)%2 == ((goal.index('_'))//size+invg)%2)
            return returner

manhattanLookup = {}
def h(puzzle, goal):
    if puzzle in manhattanLookup:
        return manhattanLookup[puzzle]
    else:
        sum = 0
        for chr in puzzle:
            if chr != "_":
                pzidx = puzzle.index(chr)
                glidx = goal.index(chr)
                sum = sum + abs(pzidx//4-glidx//4) + abs(pzidx%4-glidx%4)
        manhattanLookup[puzzle] = sum
        return sum

def hinc(nbr, pz, direction, incremDict):
    char = pz[nbr.index('_')]
    if (nbr,pz) in manhattanLookup:
        return manhattanLookup[(nbr,pz)]
    if (pz,nbr) in manhattanLookup:
        return manhattanLookup[(pz,nbr)]
    else:
        if(direction == 'U' or direction== 'D'):
            nbrrow = nbr.index(char)//4
            pzrow = pz.index(char)//4
            if abs(nbrrow-incremDict[char][0])>abs(pzrow-incremDict[char][0]):
                manhattanLookup[(nbr,pz)] = 1
                return 1
            else:
                manhattanLookup[(nbr,pz)] = -1
                return -1
        else:
            nbrrow = nbr.index(char)%4
            pzrow = pz.index(char)%4
            if abs(nbrrow-incremDict[char][1])>abs(pzrow-incremDict[char][1]):
                manhattanLookup[(nbr,pz)] = 1
                return 1
            else:
                manhattanLookup[(nbr,pz)] = -1
                return -1

def hoptimal(nbr, pz, goal,incremDict):
    char = pz[nbr.index('_')]

    newloc = pz.index('_')  # where the char is after neighbor
    oldloc = nbr.index('_')  # where the char was before neighbor

    if (char,oldloc,newloc) in manhattanLookup:
        return manhattanLookup[(char,oldloc,newloc)]
    else:
        g = incremDict[char]

        newdist = abs(newloc // 4 - g[0]) + abs(newloc % 4 - g[1])
        olddist = abs(oldloc // 4 - g[0]) + abs(oldloc % 4 - g[1])

        if(newdist>olddist):
            manhattanLookup[(nbr,pz)] = 1
            return 1
        else:
            manhattanLookup[(nbr,pz)] = -1
            return -1

def main():
    for puzzle in myL:
        print(puzzle, astar(puzzle,goal))

if __name__ == "__main__": main()

# Brian Zhou, pd 4, 2024