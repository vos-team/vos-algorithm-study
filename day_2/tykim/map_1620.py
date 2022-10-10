import sys

n, m = map(int,sys.stdin.readline().split())

name = {}
index = {}

for i in range(1, 1 + n):
    pokemon = sys.stdin.readline().strip()
    name[i] = pokemon
    index[pokemon] = i
    
for _ in range(m):
    q = sys.stdin.readline().strip()
    if q.isdigit():
        print(name[int(q)])
    else:
        print(index[q])