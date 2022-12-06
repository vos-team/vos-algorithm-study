import sys
from collections import deque

input = sys.stdin.readlines()

# n, m = input[0].split()
a1 = list(map(int, input[1].split()))
a2 = list(map(int, input[2].split()))

# print(a1, a2)
# result = ""
# e1 = a1.popleft()
# e2 = a2.popleft()
# while a1 or a2:
#     if e1 < e2:
#         result += f"{e1} "
#         e1 = a1.popleft()
#     else:
#         result += f"{e2} "
#         e2 = a2.popleft()
# print(result.strip())
print(" ".join(map(str, sorted(a1 + a2))))
