import sys
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

def quick_sort(arr):
    if len(arr) <= 1: return arr
    pivot, tail = arr[0], arr[1:]
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

n = int(input())
num_array = []

[num_array.append(int(input())) for i in range(n)]
[print(x) for x in quick_sort(num_array)]