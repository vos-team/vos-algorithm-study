# 배낭문제 행렬 형태로 문제를 풀어야 함
import sys

N = int(sys.stdin.readline())
hp = [0] + list(map(int, sys.stdin.readline().strip().split()))
happy = [0] + list(map(int, sys.stdin.readline().strip().split()))

# 100보다 작거나 같아야 됨. 
matrix = [[0] * 100 for _ in range(N+1)]

for i in range(1, N+1): 
    for j in range(1, 100):
        hpD = hp[i]
        happyG = happy[i]
        if j < hpD:
            matrix[i][j] = matrix[i - 1][j]
        else:
            matrix[i][j] = max(happyG + matrix[i - 1]
                               [j - hpD], matrix[i - 1][j])

print(matrix[-1][-1])