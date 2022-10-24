# n 개의 숫자
n = int(input())
# 빈 리스트에 입력값을 받아주기
s = []
for _ in range(n):
    s.append(int(input()))
# 정렬해주기
s.sort()
# 하나씩 출력
for x in s:
    print(x)