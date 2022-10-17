from collections import deque
# 테스트 케이스 수
t = int(input())

for i in range(t):
    # 문서의 개수(n)와 몇 번째로 인쇄되는지 궁금한 문서(m)
    n, m = map(int,input().split())
    # 중요도를 deque로 넣어주기
    queue = deque(list(map(int, input().split())))

    answer = 0
    
    while True:
        import_max = max(queue)
        front = queue.popleft()
        m -= 1

        if import_max == front:
            answer += 1
            if m < 0:
                print(answer)
                break
        else:
            queue.append(front)
            if m < 0 :
                m = len(queue) - 1