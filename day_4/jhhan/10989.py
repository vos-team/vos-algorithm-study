import sys

MAX = 10001
n = int(sys.stdin.readline())
count = [0] * MAX

for i in range(n):
    count[int(sys.stdin.readline())] += 1
    
for i in range(MAX):
    for j in range(count[i]):
      sys.stdout.write(str(i)+"\n")
