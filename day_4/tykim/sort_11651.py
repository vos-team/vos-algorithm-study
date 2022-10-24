
## dicionary는 key값이 중복이 될 수 없음
# n = int(input())

# x = []
# y = []

# for _ in range(n):
#     a,b = map(int,input().split())
#     x.append(a)
#     y.append(b)

# dic = {}

# for i in range(n):
#     dic[x[i]] = y[i]

# list로 진행
n = int(input())

point = []

for _ in range(n):
    a,b = map(int,input().split())
    # 바꿔서 저장 후 sort
    point.append([b, a])

point.sort()

for a, b in point:
    print(b, a)