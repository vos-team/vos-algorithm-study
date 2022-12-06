import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())

course_map = defaultdict(list)

for _ in range(m):
    a, b = map(lambda c: int(c) - 1, sys.stdin.readline().split())
    # print(a, b)
    course_map[b].append(a)

# print(course_map)
dp_array = [0] * n


def dp(cource):
    if dp_array[cource]:
        return dp_array[cource]
    else:
        prereqs = course_map[cource]
        # print(cource, prereqs)
        # print(dp_array)
        if len(prereqs):
            answer = max([dp(prereq) for prereq in prereqs]) + 1
            dp_array[cource] = answer
            return answer
        else:
            dp_array[cource] = 1
            return 1


print(" ".join([str(dp(cource)) for cource in range(n)]))
