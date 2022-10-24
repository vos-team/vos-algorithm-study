import sys

from collections import defaultdict

cnt = int(sys.stdin.readline())
strings = defaultdict(set)

for _ in range(cnt):
    string = sys.stdin.readline().strip()
    strings[len(string)].add(string)

for k in sorted(strings.keys()):
    for s in sorted(strings[k]):
        print(s)

# strings = list(set((line.strip() for line in sys.stdin.readlines())))


# def quicksort(strings):
#     if len(strings):
#         p = strings[0]
#         lower = []
#         upper = []

#         for string in strings[1:]:
#             if len(string) < len(p):
#                 lower.append(string)
#             elif len(string) > len(p):
#                 upper.append(string)
#             else:
#                 if string < p:
#                     lower.append(string)
#                 else:
#                     upper.append(string)
#         return quicksort(lower) + [p] + quicksort(upper)
#     return strings


# for string in quicksort(strings):
#     print(string)
