import sys

def input():
    return sys.stdin.readline().rstrip()

def next_permutation(arr):
    i = j = k = len(arr) - 1

    # arr[i-1] >= arr[i]가 되는 i 중 가장 큰 값 찾기
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1

    # i가 0이라면 모든 값이 역순이라는 뜻이기 때문에 False 반환
    if i <= 0:
        return False

    # arr[i-1] >= arr[j]가 되는 j를 찾기
    while arr[i-1] >= arr[j]:
        j -= 1

    # i번째 값과 j 번째 값을 스왑
    arr[i-1], arr[j] = arr[j], arr[i-1]

    # arr의 i번째 부터 끝까지 원소를 스왑
    while i < k:
        arr[i], arr[k] = arr[k], arr[i]
        i += 1
        k -= 1
    return True

def TSP(a, w):
    cost = 0
    for i in range(len(a)-1):
        if w[a[i]][a[i+1]] == 0:
            return False
        else:
            cost += w[a[i]][a[i+1]]
    if w[a[-1]][a[0]] == 0:
        return False
    else:
        cost += w[a[-1]][a[0]]
        return cost

def main():
    n = int(input())
    w = [list(map(int,input().split())) for _ in range(n)]
    a = [n for n in range(n)]
    minCost = sys.maxsize
    while True:
        cost = TSP(a, w)
        if cost != False:
            if cost < minCost:
                minCost = cost
        if not next_permutation(a):
            break
        if a[0] != 0:
            break
    print(minCost)
main()