import sys
from itertools import combinations

n = list(map(str, sys.stdin.readline().strip()))
answer = set() # 이름이 answer 인 set을 생성
stack = [] 
temp = [] 

# 반복문을 통해 괄호의 시작점과 끝점을 저장
for idx, word in enumerate(n): #enumerate : 리스트와 원소와 인덱스를 동시에 loop
    if word == "(":
        stack.append(idx) #왼쪽괄호에 해당하면 인덱스를 stack 리스트에 저장
    elif word == ")":
        temp.append((stack.pop(), idx)) #오른쪽괄호에 해당하면 temp리스트에 
                                        #stack 의 마지막 요소를 꺼내고 idx 넣음
# combinations을 통해 모든 경우의 수를 확인
for i in range(1, len(temp) + 1): # i 1:len(temp)+1 범위에서 
	  c = combinations(temp, i) #temp사이의 i개의 조합을 이터레이트로 변환
         
    # 반복문을 통해 경우의 수를 확인
    for j in c: # 각조합에 대해 리스트로 만들어주고
        target = list(n) 

    # 괄호 제거
        for k in j:
           target[k[0]] = ""
           target[k[1]] = ""

        answer.add(''.join(target)) #answer에 저장 
        # set.add: 요소추가, string.join: 문자열붙이기

for ans in sorted(list(answer)): #answer 리스트에 대해 정렬해서 출력하기 
    print(ans)
