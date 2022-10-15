import sys

n = int(sys.stdin.readline().rstrip())
points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
for x,y in sorted(points, key = lambda p : (p[1],p[0])):
    print(x, y, sep=" ")