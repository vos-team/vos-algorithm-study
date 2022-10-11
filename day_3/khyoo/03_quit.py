import sys

getLine = lambda: sys.stdin.readline().strip()

N = int(getLine())

dp_arr = [0] * (
    N + 1
)  # 배열의 개수를 입력받은 날짜보다 1개 크게 만들어서 마지막날까지 일을 한 경우가 맨 마지막 칸에 들어갈 수 있도록 함.

for i in range(0, N):  # 입력의 개수만큼 돌면서
    T, P = map(int, getLine().split())

    after_work_p = dp_arr[i] + P  # 해당 날짜(i)에 일을 할 경우 얻을 수 있는 금액
    if i + T < N + 1:  # 앞으로 퇴사까지 남은 날 안에 일을 끝마칠 수 있으면
        for j in range(i + T, N + 1):  # 일을 끝낸 뒤 날짜부터 배열 끝까지
            dp_arr[j] = max(dp_arr[j], after_work_p)
            # max( T시간(날짜)_이후_기존에_계산했던_최대이득, 해당_날짜(i)_까지의_최대이득_+_해당날짜의_일을_한_뒤_이득의_합계 ) 값으로 바꿔줌.

print(dp_arr[-1])
