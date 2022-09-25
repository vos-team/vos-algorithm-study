# 덱, 리스트 시간복잡도 차이 https://wellsw.tistory.com/122
# 양방향 연결 리스트로 구현하는 큐 https://sg-data.tistory.com/25

import sys
from collections import deque

n = int(input())

for _ in range(n*2):
    if _ % 2 == 0:
        req = sys.stdin.readline().strip()
        queue_num, object_order = list(int(_) for _ in req.split(' '))
    else:
        req = sys.stdin.readline().strip()
        queue = list(int(_) for _ in req.split(' '))
        deq = deque(list([value, idx] for idx, value in enumerate(queue)))
        res = list()
        while deq:
            value = deq.popleft()
            if any(rest[0] > value[0] for rest in deq):
                deq.append(value)
            else:
                res.append(value[1])

        print(res.index(object_order)+1)