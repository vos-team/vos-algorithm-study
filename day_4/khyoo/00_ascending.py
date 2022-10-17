import sys

nums = list(map(int, sys.stdin.readlines()))
cnt = nums[0]

# for num in sorted(nums[1:]):
#     print(num)

sys.setrecursionlimit(10000**2)


def quicksort(nums):
    if len(nums):
        p = nums[0]
        lower = []
        upper = []

        for num in nums[1:]:
            if num < p:
                lower.append(num)
            else:
                upper.append(num)
        return quicksort(lower) + [p] + quicksort(upper)
    return nums


for num in quicksort(nums[1:]):
    print(num)
