import sys
sys.stdin = open('day_4/mjjo/11651.txt')

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for _ in sorted(arr, key=lambda x: (x[1], x[0])):
    print(_[0], _[1])