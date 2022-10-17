import sys

nums = list(map(int, sys.stdin.readlines()))
cnt = nums[0]
for num in sorted(nums[1:]):
    print(num)
