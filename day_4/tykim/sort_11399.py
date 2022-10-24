n = int(input())

take_time = list(map(int, input().split()))

take_time.sort()

cal = 0
cal_sum = 0

for i in take_time:

    cal += i
    cal_sum += cal

print(cal_sum)