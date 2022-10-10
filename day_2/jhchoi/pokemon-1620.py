import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

nameDict, numDict = {}, {}

for number in range(1, N+1): 
    name = input()
    nameDict[name], numDict[str(number)] = number, name

for m in range(M):
    quiz = input()
    print(numDict.get(quiz)) if quiz.isnumeric() else print(nameDict.get(quiz))