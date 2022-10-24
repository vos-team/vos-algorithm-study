import sys
from itertools import permutations
sys.stdin = open('day_5/mjjo/10971.txt')

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_cost = 100000000 # sys.maxsize로 해도 됨 == 9223372036854775807

# 1
for l in permutations([_ for _ in range(N)], N):
    idx, sum = 0, 0
    is_true = True
    while idx < len(l):
        try:
            i, j = l[idx], l[idx+1]
        except:
            i, j = l[idx], l[0]
        if arr[i][j]:
            sum += arr[i][j]
        else:
            is_true = False
            break
        idx += 1

    if is_true and min_cost > sum:
        min_cost = sum

print(min_cost)

# 10! = 3628800
# 3628800 * 10 = 36288000
# 2초이므로 초당 2천만번으로 계산하면 빡빡함
# pypy3로 통과되긴 하나, 다른 방법으로 하는것이 더 좋을 듯


# 2
count = 0
def dfs_backtracking(start, curr, value, visited):
    global min_cost, count

    if len(visited) == N:
        # print(curr, start, arr[curr][start])
        if arr[curr][start] != 0:
            min_cost = min(min_cost, value + arr[curr][start])
        return

    for i in range(N):
        if (arr[curr][i] != 0) & (i not in visited) & (value < min_cost):
            visited.append(i)
            dfs_backtracking(start, i, value + arr[curr][i], visited)
            visited.pop()

for i in range(N):
    dfs_backtracking(i, i, 0, [i], )

print(min_cost)
