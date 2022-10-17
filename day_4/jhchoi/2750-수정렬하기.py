import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
num_array = []

[num_array.append(int(input())) for i in range(n)]
[print(x, end = ' ') for x in sorted(num_array)] # sorted library로 정렬