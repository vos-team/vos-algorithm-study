# https://www.acmicpc.net/problem/10828

import sys

l = lambda: sys.stdin.readline().strip()

s = []

funcs = {
    "p": (
        lambda cmd: s.append(int(cmd.split()[-1]))
        if cmd.startswith("pu")
        else print(s.pop() if len(s) else -1)
    ),
    "t": lambda cmd: print(s[-1] if len(s) else -1),
    "s": lambda cmd: print(len(s)),
    "e": lambda cmd: print(0 if len(s) else 1),
}
# def push(i):
#     s.append(i)


# def top():
#     print(s[-1] if len(s) else -1)


# def size():
#     print(len(s))


# def empty():
#     print(0 if len(s) else 1)


# def pop():
#     print(s.pop() if len(s) else -1)


n = int(l())
for _ in range(n):
    cmd = l()
    funcs[cmd[0]](cmd)
    # if cmd.startswith("pu"):
    #     _, num = cmd.split()
    #     push(int(num))
    # else:
    #     {"t": top, "s": size, "e": empty, "p": pop}[cmd[0]]()
