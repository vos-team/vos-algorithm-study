import sys
n = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(n)]
[sys.stdout.write(str(i)+"\n") for i in sorted(array)]