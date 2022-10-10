import sys

getLine = lambda: sys.stdin.readline().strip()

n = int(getLine())
efforts = list(map(int, getLine().split()))
joys = list(map(int, getLine().split()))

init_energy = 100
init_joy = 0
states = [[(init_energy, init_joy)]]

max_joy_sum = 0
for i in range(1, n + 1):
    e, j = efforts[i - 1], joys[i - 1]
    curr_state = []
    states.append(curr_state)
    for prev_e, prev_j in states[i - 1]:
        if prev_e - e > 0:
            curr_e, curr_j = prev_e - e, prev_j + j
            curr_state.append((curr_e, curr_j))
            if curr_j > max_joy_sum:
                max_joy_sum = curr_j
        curr_state.append((prev_e, prev_j))

# for state in states:
#     for e, j in state:
#         if j > max_joy_sum:
#             max_joy_sum = j

print(max_joy_sum)
