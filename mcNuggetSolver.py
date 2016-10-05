vals = [6, 9, 20]
vals.sort()
sol = [False]*(reduce(lambda x, y: x*y, vals) + 1)
for i in vals:
    sol[i] = True

runLength = 0
index = -1
for i in range(len(sol)):
    if(sol[i]):
        runLength += 1
        if(runLength >= vals[0]):
            break
        for v in vals:
            sol[i+v] = True
    else:
        runLength = 0
        index = i

print index
