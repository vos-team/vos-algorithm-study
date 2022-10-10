# dp문제는 중복된 하위 문제들이 존재할때 사용함.
# 점화식을 먼저 만들고 진행
# dp[i] = min(dp[i//3], dp[i//2], dp[i-1]) + 1

import sys

sys.setrecursionlimit(10**6)

n = int(input())

dp = [0]*(n+1) # 0번째를 사용하지않고 1번부터 사용

# 1은 1번도 진행을 하지 않아도 되기 때문에 그대로 return 0
for i in range(2, n+1):

    if i % 3 == 0:

        if i % 2 == 0: # 3으로 나누어 떨어지는것과 2로도 나누어떨어진다면 최솟값 넣어주기

            dp[i] = min(dp[i//2], dp[i//3], dp[i-1])+1

        else: # 3으로만 나누어진다면 2를 제외한 두가지의 최솟값

            dp[i] = min(dp[i//3], dp[i-1])+1

    elif i % 2 == 0: #2로만 나누어 떨어지는 경우

        dp[i] = min(dp[i//2], dp[i-1])+1

    else: # 3과 2 둘다 안나누어 진다면 그 전 값에 +1

        dp[i] = dp[i-1]+1

print(dp[n])
