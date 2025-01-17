import sys; args = sys.argv[1:]
import time; startTime = time.time()
import math;

start = args[0]; 
size = int(math.sqrt(len(start)))
if len(args)>1: goal = args[1] 
else: goal = '12345678_'

def solve(start, goal):
    path = []
    parseMe=[start]
    detSeen = {start:'end'}
    if start==goal: return [start]
    for i in parseMe:
        for n in neighbors(i):
            if n not in detSeen:
                parseMe.append(n)
                detSeen[n] = i
                if n==goal: 
                    path.append(n)
                    while detSeen[n] != 'end': 
                        path.append(detSeen[n])
                        n = detSeen[n]
                    return path[::-1]
    return []

lookup = {}

def neighbors(s):
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

def band(l):
    if (len(l) > 9): 
        s = "" + band(l[:9]) + '\n' + band(l[9:])
        return s
      
    s = ""
    for i in range(size): 
        for j in range(len(l)):
            s += l[j][i * size: i * size + size] + " "
        s += '\n'
    return s

def inversionct(str):
    count = 0; 
    for left in range(size**2):
        for right in range(left, size**2):
            if str[left] =='_' or str[right] == '_': continue
            if str[left] > str[right]: count = count + 1
    return count

def isSolvable(start,goal):
    invs = inversionct(start); invg = inversionct(goal)
    if size % 2: 
        return invs % 2 == invg % 2 # if even
    else: 
        return (invs + start.find('_') - invg - goal.find('')) % 2 == 0 # if even

if isSolvable(start,goal): #if solvable:
    l = solve(start,goal)
else:
    l = []

if len(l): print(band(l))
else: print(band([start]))

print('Steps: ' + str(len(l)-1))
print('Time: ' + f"{(time.time()-startTime):.3}s")

# Brian Zhou, pd 4, 2024