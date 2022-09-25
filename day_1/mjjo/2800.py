import re
import sys
from itertools import combinations

req = str(input())
req_arr = list(map(str, req))
res_arr = set()
comb_arr = list()
bracket_length = len(re.findall(r'\(', req))
bracket_arr = list(range(1, bracket_length + 1))
open_stack = list()
order_arr = list()

for idx, value in enumerate(req_arr):
    if value == '(':
        open_stack.append(idx)
    if value == ')':
        order_arr.append([open_stack.pop(), idx])

order_arr = sorted(order_arr)

for i in bracket_arr:
    for comb in combinations(bracket_arr, i):
        res_req = list(req)
        for del_bracket_order in comb:
            open_idx, close_idx = order_arr[del_bracket_order-1]
            res_req[open_idx] = '@'
            res_req[close_idx] = '@'
        res_arr.add(''.join(res_req).replace('@', ''))

for res in sorted(res_arr):
    print(res)