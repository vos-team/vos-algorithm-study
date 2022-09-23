import sys
import itertools

str = sys.stdin.readline().rstrip()

# 1. 괄호 짝index를 튜플로 저장
left_stack = []
pair_tuple = []

for idx, char in enumerate(str):
  if char == '(' :
    left_stack.append(idx)
  elif char == ')':
    if len(left_stack):
      pair_tuple.append((left_stack.pop(), idx))
      
# 2. 괄호 짝으로 만들 수 있는 모든 경우의 수를 순회
num_arr = list(range(0, len(pair_tuple))) # 0,1,2,3 ... n
ans_set = set()

for i in num_arr:
  str_clone = str
  for pos_arr in list(map(list,itertools.combinations(num_arr, i+1))): # [][]
    check = [False] * len(str)
    for pos in pos_arr: # []
      left, right = pair_tuple[pos]
      check[left] = True
      check[right] = True
      
    result = []    
    for j in range(0, len(str)):
      if not check[j] :
        result.append(str[j])
        
    ans_set.add(''.join(result))
      
# 3. 결과는 set에 저장해두고 sort 해서 추력
for ans in sorted(ans_set):
  print(ans)