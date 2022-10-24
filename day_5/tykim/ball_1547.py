# n 개의 숫자
n = int(input())
# 처음 공이 놓인 위치
key = 1
# 컵의 번호를 리스트에 넣어주기
ball = []
for i in range(n):
    a, b = map(int,input().split())
    ball.append([a, b])
    
    #0번째에 key가 있으면 1번째로 key를 넘겨주고 아니면 반대로
    if ball[i][0] == key:
        key = ball[i][1]
    elif ball[i][1] == key:
        key = ball[i][0]
        
print(key)