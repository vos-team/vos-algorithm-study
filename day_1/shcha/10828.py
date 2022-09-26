import sys

def input():  # 입력에 대한 동일한 설정을 가진 새로운 함수 정의
    return sys.stdin.readline().rstrip() #sys 모듈의 readline()을 사용, 오른쪽 공백제거

def print_size(x): #리스트의 크기를 반환하는 함수 만듦
    return len(x) 

N = int(input()) 

stack = []
for n in range(N): #입력된 숫자 N에 대해 0:N-1 범위내의 for문형태로 구현하는 이유? -> 입력의 갯수를 제한
    command = input().split() #띄어쓰기를 기준으로 입력받은 글자를 쪼개서 저장한다. command[0]은 push, top 등이 된다.
    if(command[0] == 'push'):
        stack.append(int(command[1])) #command[1]의 값을 리스트에 추가해준다
    elif(command[0] == 'pop'):
        print(-1 if print_size(stack) == 0 else stack.pop())
    elif(command[0] == 'size'): 
        print(print_size(stack)) #size 입력시 stack의 크기 출력
    elif(command[0] == 'empty'): 
        print(1 if print_size(stack) == 0 else 0) #empty 입력시 사이즈가0이라면 1을 출력 그렇지 않음 0
    elif(command[0] == 'top'): 
        print(-1 if print_size(stack) == 0 else stack[-1])
