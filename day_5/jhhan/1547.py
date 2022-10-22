import sys

ball_pos = 1
m = int(sys.stdin.readline())

for i in range(m):
  s, e = map(int, sys.stdin.readline().split())
  if ball_pos == s: ball_pos = e 
  elif ball_pos == e: ball_pos = s

print(ball_pos)