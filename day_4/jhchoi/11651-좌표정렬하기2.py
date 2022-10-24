import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
arr = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append([y,x]) # y를 우선 순위로 정렬 시키기 위해서 y, x 순으로 리스트에 넣어줌

[print(x, y) for y, x in sorted(arr)]