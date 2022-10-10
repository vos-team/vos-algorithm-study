import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {} #딕셔너리 정의, key : value 구조를 가짐

for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a #for의 각 키값 (i) 에 입력되는 포켓몬이름을 value로 저장
    dict[a] = i #포켓몬 이름으로도 키값을 만들고 이때 value는 i

for i in range(m):
    quest = input().rstrip() #입력받은 문자열이
    if quest.isdigit(): #숫자인경우
        print(dict[int(quest)]) #해당하는 포켓몬 이름을 출력
    else:
        print(dict[quest]) #그렇지 않으면 포켓몬의 번호 출력
