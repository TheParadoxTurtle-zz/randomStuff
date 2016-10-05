import math

N = int(raw_input())
M = int(raw_input())
D_line = raw_input()
D_line = D_line.split()
d = map(lambda x: float(x), D_line)
triangles = [None]*N

for i in range(N):
    line = raw_input()
    line = line.split()
    triangles[i] = map(lambda x: int(x), line)

ships = [None]*M

for i in range(M):
    line = raw_input()
    line = line.split()
    ships[i] = map(lambda x: float(x), line)


def subtract(v1, v2):
    v = [0, 0, 0]
    v[0] = v1[0] - v2[0]
    v[1] = v1[1] - v2[1]
    v[2] = v1[2] - v2[2]
    return v


def mul(v1, s):
    v = [v1[0]*s, v1[1]*s, v1[2]*s]
    return v


def cross(v1, v2):
    v = [0, 0, 0]
    v[0] = v1[1]*v2[2] - v1[2]*v2[1]
    v[1] = v1[2]*v2[0] - v1[0]*v2[2]
    v[2] = v1[0]*v2[1] - v1[1]*v2[0]
    return v


def dot(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]


def norm(v):
    return math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2])


def normalize(v):
    n = norm(v)
    v_n = [v[0]/n, v[1]/n, v[2]/n]
    return v_n

norms = [None]*N
for i in range(N):
    x = ships[triangles[i][0]]
    y = ships[triangles[i][1]]
    z = ships[triangles[i][2]]
    v1 = subtract(y, x)
    v2 = subtract(z, x)
    norms[i] = cross(v1, v2)
    norms[i] = normalize(norms[i])


def inside(t, p):
    tri = triangles[t]
    x = ships[tri[0]]
    y = ships[tri[1]]
    z = ships[tri[2]]
    v0 = subtract(y, x)
    v1 = subtract(z, y)
    v2 = subtract(x, z)
    r0 = subtract(p, y)
    r1 = subtract(p, z)
    r2 = subtract(p, x)
    s0 = 1 if cross(v0, r0) >= 0 else -1
    s1 = 1 if cross(v1, r1) >= 0 else -1
    s2 = 1 if cross(v2, r2) >= 0 else -1
    return s0 == s1 == s2


def inbetween(p, a, b):
    if (a[0] <= p[0] <= b[0]) or (b[0] <= p[0] <= a[0]):
        if (a[1] <= p[1] <= b[1]) or (b[1] <= p[1] <= a[1]):
            if (a[2] <= p[2] <= b[2]) or (b[2] <= p[2] <= a[2]):
                return True
    return False


def dist(p1, p2):
    return norm(subtract(p1, p2))


def closest_point(t, p):
    tri = triangles[t]
    x = ships[tri[0]]
    y = ships[tri[1]]
    z = ships[tri[2]]
    v0 = normalize(subtract(y, x))
    v1 = normalize(subtract(z, y))
    v2 = normalize(subtract(x, z))
    h0 = subtract(p, x)
    h1 = subtract(p, y)
    h2 = subtract(p, z)
    d0 = subtract(h0, mul(v0, dot(h0, v0)))
    d1 = subtract(h1, mul(v1, dot(h1, v1)))
    d2 = subtract(h2, mul(v2, dot(h2, v2)))
    p0 = subtract(p, d0)
    p1 = subtract(p, d1)
    p2 = subtract(p, d2)
    min_dist = 20
    point = None
    if inbetween(p0, x, y):
        temp = dist(p, p0)
        if min_dist > temp:
            min_dist = temp
            point = p0
    if inbetween(p1, y, z):
        temp = dist(p, p1)
        if min_dist > temp:
            min_dist = temp
            point = p1
    if inbetween(p2, z, x):
        temp = dist(p, p2)
        if min_dist > temp:
            min_dist = temp
            point = p2
    temp = dist(p, x)
    if min_dist > temp:
        min_dist = temp
        point = x
    temp = dist(p, y)
    if min_dist > temp:
        min_dist = temp
        point = y
    temp = dist(p, z)
    if min_dist > temp:
        min_dist = temp
        point = z
    return point


min = 11
t = N+1


for i in range(N):
    v = subtract(d, ships[triangles[i][0]])
    min_dist = abs(dot(v, norms[i]))
    if min_dist > min:
        continue
    proj = subtract(d, mul(norms[i], min_dist))
    if not inside(i, proj):
        c = closest_point(i, proj)
        min_dist = dist(c, d)
    if min_dist == min:
        if i < t:
            t = i
        continue
    min = min_dist
    t = i
print "%.2f" % min
print t
