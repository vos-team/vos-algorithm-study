# https://www.acmicpc.net/problem/2800
from itertools import combinations
import sys

l = lambda: sys.stdin.readline().strip()

input = l()
st = []
p_pairs = []

for i, c in enumerate(input):
    if c == "(":
        st.append([i, -1])
    elif c == ")":
        st[-1][1] = i
        p_paired = st.pop()
        p_pairs.append(p_paired)

results = set()
for r in range(1, len(p_pairs) + 1):
    for comb in combinations(p_pairs, r):
        p_locs = sum(comb, [])
        result = "".join([c for i, c in enumerate(input) if i not in p_locs])
        results.add(result)

for result in sorted(results):
    print(result)
