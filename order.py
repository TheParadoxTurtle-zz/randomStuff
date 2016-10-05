n = 72
factors = [2, 3]

for i in range(1, 72):
    coprime = True
    for f in factors:
        if i % f == 0:
            coprime = False
            break
    if not coprime:
        continue
    v = i
    p = 1
    while v != 1:
        v *= i
        v %= n
        p += 1
    print i, p
