import sys
sys.stdin = open("day_5/mjjo/1547.txt")

input = sys.stdin.readline
N = int(input())
tc = [1, 0, 0]
arr = [list(map(int, input().split())) for _ in range(N)]
for cups in arr:
    i, j = cups[0] -1, cups[1] -1
    tc[i], tc[j] = tc[j], tc[i]

print(tc.index(1) + 1)