# import sys

# INF = 10**7+1

# n = int(sys.stdin.readline())
# arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
# dp=[[INF] * n for _ in range(2**n+1)]

# def dfs(visit_bit, cur_city, cost):
#   for i in range(n):
#     # cur_city -> i 시티로 갈 수 있는지 부터 확인
#     if arr[cur_city][i] == 0 :
#       continue
    
#     # i 번째 도시 방문하였는가 ?
#     isVisited = 1 if visit_bit & (1 << i) != 0 else 0
#     next_visit_bit = visit_bit | (1<<i)
#     next_visit_cost = cost + arr[cur_city][i]
    
#     # 이미 방문한 곳은 갈수 없음.
#     if not isVisited :
#       # 더 최적의 비용이면 탐색 진행
#       if dp[next_visit_bit][i] > next_visit_cost : 
#         dp[next_visit_bit][i] = next_visit_cost 
#         dfs(next_visit_bit, i, next_visit_cost)
        
# dfs(0, 0, 0)
# print(min(dp[2**n-1]))


import sys
INF = 10**7+1

n = int(sys.stdin.readline())
arr = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
dp=[[INF] * n for _ in range(1<<n)]

def dfs(visit_bit, cur_city):
  # 방문 표시
  visit_bit |= (1<<cur_city)
  
  # 도착 
  if visit_bit == (1 << n) - 1:
    return arr[cur_city][0] if arr[cur_city][0] > 0 else INF;
  
  # 방문한적 있다면 dp 값 재활용
  if dp[visit_bit][cur_city] != INF:
    return dp[visit_bit][cur_city]
 
  for next_city in range(n):
    # 미방문 & 방문가능한 경우
    if visit_bit & (1 << next_city) == 0 and arr[cur_city][next_city] > 0:
      # 현재경로에서 다음 도시 방문한 경우와 dp값 비교해서 갱신
      dp[visit_bit][cur_city] = min(dp[visit_bit][cur_city], dfs(visit_bit, next_city) + arr[cur_city][next_city])
        
  return dp[visit_bit][cur_city]

print(dfs(0, 0))