import sys
from itertools import permutations
sys.stdin = open('day_5/mjjo/10971.txt')

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min = 100000000 # sys.maxsize로 해도 됨 == 9223372036854775807

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

    if is_true and min > sum:
        min = sum

print(min)

# 10! = 3628800
# 3628800 * 10 = 36288000
# 2초이므로 초당 2천만번으로 계산하면 빡빡함
# pypy3로 통과되긴 하나, 다른 방법으로 하는것이 더 좋을 듯