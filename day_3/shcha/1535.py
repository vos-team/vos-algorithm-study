N = int(input())
L = [int(x) for x in input().split()] #체력손실
J = [int(x) for x in input().split()] #얻는기쁨
L, J = [0] + L, [0] + J # 리스트 맨앞에 원소 0을 추가해줌
dp = [[0 for _ in range(101)] for _ in range(N+1)] 
#0이 101개 들어있는 리스트를 N+1만큼 만들어줌 

for i in range(1, N+1):
    for j in range(1, 101):
        if L[i] <= j: #얻는 기쁨이 체력손실보다 같거나 크다면
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]] + J[i])
        else: #그렇지 않은경우 인사하지않고 이전 사람에게 인사했을때까지 얻은 기쁨 불러옴
            dp[i][j] = dp[i-1][j]

print(dp[N][99])
