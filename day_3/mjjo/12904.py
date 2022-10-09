import sys

sys.stdin = open("day_3/mjjo/12904.txt")
input = sys.stdin.readline


# 1 
# 모든 경우의 수 생성 >>> 메모리 초과
S, T = input().strip(), input().strip()

res = [set() for _ in range(len(T)+1 - len(S))]
res[0] = set(S)

for i in range(len(res)-1):
        for j in res[i]:
            res[i+1].add(j +'A')
            res[i+1].add(j[::-1] +'B')

print(1) if T in res[-1] else print(0)


# 2
# 1과 반대 순서로 처리 T > S
# 리스트로 처리
S, T = input().strip(), [_ for _ in input().strip()]

# A로 끝나면 뒤에서 A를 제거
# B로 끝나면 뒤에서 B를 제거하고 뒤집기
for i in range(len(T) - len(S)):
    last_str = T.pop()
    if last_str == 'B':
        T = T[::-1]

print(1) if S == ''.join(T) else print(0)


# 3 문자열로 처리
S, T = input().strip(), input().strip()

for i in range(len(T) - len(S)):
    if T[-1] == 'B':
        T = T[:-1][::-1]
    else:
        T = T[:-1]

print(1) if S == T else print(0)