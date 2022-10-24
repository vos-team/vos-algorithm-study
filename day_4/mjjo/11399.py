import sys
sys.stdin = open('day_4/mjjo/11399.txt')

input = sys.stdin.readline
dp = [0] * (int(input()) + 1)
arr = [[_, idx] for idx, _ in enumerate(map(int, input().split()))]

for idx, v in enumerate(sorted(arr)):
    dp[idx+1] = dp[idx] + v[0]

print(sum(dp))