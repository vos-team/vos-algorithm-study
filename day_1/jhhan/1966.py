import sys
import collections

t = int(sys.stdin.readline().rstrip())

for i in range(t):
  # n : 문서 개수 (1~100)
  # m : 인쇄순번 궁금한 문서index
  n, m = list(map(int,sys.stdin.readline().split()))

  # p : 중요도 리스트 (1~9)
  p = list(map(int,sys.stdin.readline().split()))
  
  if len(p) == 1 :
    print(1)
    continue
  
  deque = collections.deque(zip(p,[0] * n))
  deque[m] = (deque[m][0], 1)

  sorted_p = sorted(p)
  print_cnt = 0
  
  # n번만큼 돌려서 타겟을 마지막으로 위치 이동
  while True:
    if sorted_p[-1] == deque[0][0] :
      print_cnt +=1
      sorted_p.pop()
      if(deque.popleft()[1] == 1):
        print(print_cnt)
        break
    else : 
      deque.rotate(-1) # 왼쪽으로 회전
      
  