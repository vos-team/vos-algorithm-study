arr = [1, 2, 3]
for _ in range(int(input())):
    x, y = map(int, input().split())
    x_idx, y_idx = arr.index(x), arr.index(y)
    arr[x_idx], arr[y_idx] = arr[y_idx], arr[x_idx]
print(arr[0])