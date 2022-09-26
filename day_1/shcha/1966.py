test_cases = int(input()) #테스트할 케이스의 수

for _ in range(test_cases):
    n,m = list(map(int, input().split(" "))) #n, m의 입력 (리스트)
    imp = list(map(int, input().split(" "))) #중요도 입력 (리스트)
    idx = list(range(len(imp))) #중요도의 길이만큼 리스트 생성 (0:len(imp))
    idx[m] = 'target' # 타겟문서

    # 순서
    order = 0 # 순서 초기화
       
    for x in imp: # 중요도 리스트를 돌면서
        if x==max(imp): # 중요도 중에서 가장 큰값인가?
            order += 1
                           
            if idx[0]=='target':
                print(order)
                break      # loop문을 빠져나옴
            else:
                imp.pop(0) # imp 의 0번째 원소를 꺼내온다
                idx.pop(0) # idx 의 0번째 원소를 꺼내온다

        else:
            imp.append(imp.pop(0)) # imp 의 0번째 원소를 리스트의 마지막에 넣는다.
            idx.append(idx.pop(0)) # idx 의 0번째 원소를 리스트의 마지막에 넣는다.
