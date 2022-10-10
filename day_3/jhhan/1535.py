import sys
n = int(sys.stdin.readline().rstrip())
health = list(map(int,sys.stdin.readline().split()))
happy = list(map(int,sys.stdin.readline().split()))

dp = [[0]*100 for _ in range(n+1)]

for i in range(0,n):
    for h in range(1, 100):
        if h >= health[i]:
            dp[i][h] = max(dp[i-1][h],dp[i-1][h-health[i]] + happy[i]) # 택한 경우
        else : 
            dp[i][h] = dp[i-1][h] # 택하지 않는 경우                                                                                
print(dp[n-1][99])