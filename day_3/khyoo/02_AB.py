import sys

getLine = lambda: sys.stdin.readline().strip()

S = getLine()
T = getLine()

minus_a = lambda s: s[:-1]
minus_b = lambda s: s[:-1][::-1]

while len(T) > len(S):
    if T[-1] == "A":
        T = minus_a(T)
    elif T[-1] == "B":
        T = minus_b(T)

if T == S:
    print(1)
else:
    print(0)
