import sys

n,m = list(map(int, sys.stdin.readline().split()))

# [포켓몬이름, 포켓몬이름...]
pocketmonList = [sys.stdin.readline().rstrip() for i in range(n)]

# { [포켓몬이름]:번호 }
pocketmonDict = dict(zip(pocketmonList, range(1, n+1)))

for i in range(m):
  question = sys.stdin.readline().rstrip()
  print(pocketmonList[int(question)-1] if question.isdigit() else pocketmonDict[question])