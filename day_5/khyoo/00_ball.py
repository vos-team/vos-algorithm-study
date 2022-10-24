import sys

change_cnt = int(sys.stdin.readline())
cups_loc = {str(i): str(i) for i in range(1, 4)}

for i in range(change_cnt):
    cup_1, cup_2 = sys.stdin.readline().split()
    cups_loc[cup_1], cups_loc[cup_2] = cups_loc[cup_2], cups_loc[cup_1]

print({v: k for k, v in cups_loc.items()}["1"])
