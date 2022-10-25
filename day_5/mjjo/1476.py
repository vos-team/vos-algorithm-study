import sys
sys.stdin = open('baekjoon/bruteforce/1476.txt')

input = sys.stdin.readline
E, S, M = map(int, input().split())
E = 0 if E == 15 else E
S = 0 if S == 28 else S
M = 0 if M == 19 else M

# print(E, S, M)
Y = 1
while 1:
    if (Y % 15 == E) & (Y % 28 == S) & (Y % 19 == M):
        print(Y)
        break
    Y += 1