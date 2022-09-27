# https://www.acmicpc.net/problem/2800
# from itertools import combinations
import sys

l = lambda: sys.stdin.readline().strip()

input = l()
st = []
p_pairs = []

for i, c in enumerate(input):
    if c == "(":
        st.append((i, -1))
    elif c == ")":
        p_paired = (st.pop()[0], i)
        p_pairs.append(p_paired)

p_pairs = sorted(p_pairs)


def getCombinations(p_pairs):
    if len(p_pairs) == 1:
        combs = [p_pairs]

    else:
        combs = (
            getCombinations(p_pairs[1:])
            + [p_pairs[:1]]
            + [p_pairs[:1] + comb for comb in getCombinations(p_pairs[1:])]
        )
    return combs


combs = getCombinations(p_pairs)

results_set = set()
results = []
for comb in combs:
    result = list(input)
    for i1, i2 in comb:
        result[i1], result[i2] = "", ""
    result = "".join(result)
    if result not in results_set:

        results_set.add(result)
        if result:
            results.append(result)
        else:
            results = [result] + results

for result in sorted(results):
    # 여기서 sorted를 안해야 하는데,, 하면 맞고 안하면 틀리네...
    print(result)
