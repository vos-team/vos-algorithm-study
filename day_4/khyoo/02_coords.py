import sys

cnt = int(sys.stdin.readline())
coords = [
    (int(y), int(x)) for x, y in map(lambda line: line.split(), sys.stdin.readlines())
]

for y, x in sorted(coords):
    print(x, y)
