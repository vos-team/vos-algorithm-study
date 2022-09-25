import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

expressions = list(map(str, input()))

stack, brackets = [], []
resultSet = set()
# 괄호쌍 찾기
for idx, ex in enumerate(expressions): 
    if ex == '(':
        stack.append(idx)
    if ex == ')':
        brackets.append((stack.pop(), idx))
# 괄호쌍 제거 조합
for i in range(len(brackets)): 
    for combination in combinations(brackets, i + 1):
        tmp = expressions[:]
        for s, e in combination:
            tmp[s], tmp[e] = '', ''
        resultSet.add(''.join(tmp))
[print(result) for result in sorted(list(resultSet))]