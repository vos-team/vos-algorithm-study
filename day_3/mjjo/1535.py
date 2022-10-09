import sys
from itertools import combinations

sys.stdin = open("day_3/mjjo/1535.txt")
input = sys.stdin.readline
n = int(input())


# 1
# combinations 적용
# 잃는 hp가 100인 값은 제외하고 input_list 생성
input_list = [(hp, happiness) for hp, happiness in zip(map(int, input().split()), map(int, input().split())) if hp < 100]
res = 0

for i in range(1, len(input_list)+1):
    for j in combinations(input_list, i):
        if sum(_[0] for _ in j) < 100:
            if res < sum(_[1] for _ in j):
                res = sum(_[1] for _ in j)

print(res)


# 2
# 잃는 hp가 100인 값은 제외하고 input_list 생성
input_list = [(hp, happiness) for hp, happiness in zip(map(int, input().split()), map(int, input().split())) if hp < 100]
dp = [0] * 100

for idx, inputs in enumerate(input_list):
    for i in range(99, inputs[0]-1, -1):
        # print(f'dp[i] : {dp[i]}, dp[i-inputs[0]] : {dp[i-inputs[0]]}, inputs[1] : {inputs[1]}')
        dp[i] = max(dp[i], dp[i - inputs[0]] + inputs[1])

print(dp[99])


# 3
input_list = [(hp, happiness) for hp, happiness in zip(map(int, input().split()), map(int, input().split())) if hp < 100]
dp = {}
def f(i, m):
    if i >= len(input_list): return 0
    if (i, m) in dp:
        return dp[i, m]
    hp, happiness = input_list[i]
    ans = max(f(i+1, m - hp) + happiness if m - hp > 0 else 0, f(i+1, m))
    dp[i, m] = ans
    return ans

print(f(0, 100))


# 계산횟수 차이 
# [(10, 3), (20, 40), (40, 23), (33, 91), (67, 28), (44, 33), (12, 6)]
# dp list로 한 경우 474회 (99-10+1) + (99-20+1) + (99-40+1) ... 
# dp dictionary로 한 경우 164회 def f 호출