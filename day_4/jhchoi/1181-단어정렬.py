import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
words = []

[words.append(input()) for _ in range(n)]

[print(word) for word in sorted(sorted(list(set(words))), key=len)]