import sys

E, S, M = map(int, sys.stdin.readline().split())
e_max, s_max, m_max = 15, 28, 19

e_start, s_start, m_start = 1, 1, 1

# print(E, S, M)
y_jg = [e_start, s_start, m_start]
y = 1

while True:
    # print(y_jg)
    # print(y)

    e_curr, s_curr, m_curr = y_jg

    if e_curr == E and s_curr == S and m_curr == M:
        print(y)
        break

    if e_curr == e_max:
        y_jg[0] = 0

    if s_curr == s_max:
        y_jg[1] = 0

    if m_curr == m_max:
        y_jg[2] = 0

    y_jg = list(map(lambda x: x + 1, y_jg))
    y += 1
