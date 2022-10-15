import sys, itertools

n = int(sys.stdin.readline())
times = sorted(map(int, sys.stdin.readline().split()))
print(sum(list(itertools.accumulate(times))))