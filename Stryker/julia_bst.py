from collections import defaultdict

n = int(raw_input())
line = raw_input()
line = line.split()
nums = map(lambda x: int(x), line)


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if val > self.val:
            if self.right is None:
                self.right = Node(val)
            else:
                return self.right.insert(val) + 1
        else:
            if self.left is None:
                self.left = Node(val)
            else:
                return self.left.insert(val) + 1
        return 0

root = Node(nums[0])
F = defaultdict(int)
for i in nums[1:]:
    depth = root.insert(i)
    F[depth] += 1

tot = 0
for key in F:
    tot += key*F[key]

print tot
