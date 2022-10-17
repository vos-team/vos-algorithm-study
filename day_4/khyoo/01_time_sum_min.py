import sys

cnt = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

times = sorted(nums)

time_sum = 0
for i in range(1, cnt + 1):
    # print(times[:i])
    time_sum += sum(times[:i])

print(time_sum)
