from collections import deque

n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]

dx = [0, 1, 0, -1] #각각 동, 북, 서, 남의 x축 방향벡터
dy = [1, 0, -1, 0] #각각 동, 북, 서, 남의 y축 방향벡터

for i in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 2

#print(graph)
l = int(input()) #방향전환횟수
dirDict = dict() #횟수와 방향을 저장하는 dictionary
queue = deque()
queue.append((0, 0)) # 뱀의 처음 위치

for i in range(l): #방향전환횟수 만큼 반복
    x, c = input().split() #시작후 x초 뒤, 방향을 입력받음  D: 오른쪽으로, L: 왼쪽으로
    dirDict[int(x)] = c #{3: 'D', 15: 'L', 17: 'D'}

x, y = 0, 0 # 뱀의 위치 초기화
graph[x][y] = 1
cnt = 0 #이동횟수
direction = 0 #방향

def turn(alpha):
    global direction
    if alpha == 'L': 
        direction = (direction - 1) % 4 #4를 나눈 나머지; 동->북->서->남
    else:
        direction = (direction + 1) % 4 #4를 나눈 나머지; 동->남->서->북


while True:
    cnt += 1 #전체 반복문 돌아갈때 마다, 뱀의 이동횟수를 추가
    x += dx[direction] #dx[0] = 0 (동쪽 이동) ....
    y += dy[direction] #dy[0] = 1 (동쪽 이동) ....
		#direction :  0 cnt : 1
		#direction :  0 cnt : 2
		#direction :  0 cnt 3
		#direction :  1 cnt 4
		#direction :  1 cnt 5
		#direction :  1 cnt 6
		#direction :  1 cnt 7
		#direction :  1 cnt 8
		#direction :  1 cnt 9
    if x < 0 or x >= n or y < 0 or y >= n: #보드의 크기를 벗어나면 종료
        break

    if graph[x][y] == 2: #방문한 칸에 사과가 있을 때
        graph[x][y] = 1 #뱀이 사과를 먹고 늘어나 뱀이 위치한다고 바꿔줌
        queue.append((x, y)) #뱀의 위치에 대해 큐에 추가한다
        if cnt in dirDict: #딕셔너리에 지정된 초에 해당이되면 turn 한다
            turn(dirDict[cnt]) 

    elif graph[x][y] == 0: #방문한 칸이 아무것도 없을 때
        graph[x][y] = 1 #뱀이 방문했으므로 1로 변경
        queue.append((x, y)) #뱀의 위치를 큐에 추가
        tx, ty = queue.popleft() #가장 처음에 있었던 뱀의 위치를 popleft
        graph[tx][ty] = 0 # 그위치에 해당하는 원소의 값을 0으로 만들어줌
        if cnt in dirDict: #딕셔너리에 지정된 초에 해당이되면 turn 한다
            turn(dirDict[cnt])

    else:
        break

print(cnt)
