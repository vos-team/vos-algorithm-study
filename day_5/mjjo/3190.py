import sys

sys.stdin = open("day_5/mjjo/3190.txt")
input = sys.stdin.readline

N = int(input())

loc_apple = [list(map(lambda x: int(x)-1, input().split())) for _ in range(int(input()))]

order_dic = {}
for _ in range(int(input())):
    turn, dir = input().split()
    order_dic[int(turn)] = dir

# 지도와 뱀, 사과를 매턴 확인하기 위한 출력 함수
def printMap(loc_apple, loc_snake):
    print_map = [['0']*N for _ in range(N)]
    for loc in loc_snake:
        print_map[loc[0]][loc[1]] = '*' # 뱀
    for loc in loc_apple:
        print_map[loc[0]][loc[1]] = 'a' # 사과
    for _ in print_map:
        print(_)

def checkBreak(loc_snake, loc_add):
    # 추가되는 머리가 밖으로 나갈경우
    if (loc_add[0] < 0) or (loc_add[0] >= N) or (loc_add[1] < 0) or (loc_add[1] >= N):
        return False
    # 추가되는 머리가 몸과 부딪칠 경우
    for loc in loc_snake:
        if loc_add == loc:
            return False
    return True

def checkEatApple(loc_apple, loc_add):
    for idx, loc in enumerate(loc_apple):
        if loc == loc_add:
            return True, idx
    return False, None

def checkOrder(turn, order_dic, dir):
    if turn in order_dic.keys():
        if order_dic[turn] == 'L': # 'L' 왼쪽으로 도는것이기 때문에 -1
            dir -= 1
        else: # 'D' 오른쪽으로 도는것이기 때문에 +1
            dir += 1
    if dir < min_dic_key: # 최대값 3보다 크면 다시 0으로 (360도)방향이므로 순환
        dir = 3
    if dir > max_dic_key: # 최소값 0보다 작으면 다시 0으로 (360도)방향이므로 순환
        dir = 0
    return dir

loc_snake = [[0, 0]]
turn = 0
dir = 1 # 초기방향 오른쪽
dir_dic = { # 시계방향으로 top - right - bottom - left
    0: [-1, 0], # top
    1: [0, 1], # right
    2: [1, 0], # bottom
    3: [0, -1], # left
}
min_dic_key = 0
max_dic_key = 3

while 1:
    # 매턴 출력 확인용
    print('turn : ', turn)
    print('location_apple : ', loc_apple)
    print('location_snake : ', loc_snake)
    printMap(loc_apple, loc_snake)

    # turn과 order를 확인해서 방향 확인
    dir = checkOrder(turn, order_dic, dir)
    
    # 머리가 움질일 다음 칸
    loc_add_x, loc_add_y = loc_snake[-1][0] + dir_dic[dir][0], loc_snake[-1][1] + dir_dic[dir][1]
    loc_add = [loc_add_x, loc_add_y]
    # 머리가 움직일 다음 칸에 사과유무와 사과가 있다면 사과의 idx
    is_true, idx = checkEatApple(loc_apple, loc_add)
    
    # 테스트해보니 pop보다 append와 break check(맵 나가는지, 몸과 접하는지)를 해야 문제의도에 맞게 나와서 이 순서 대로 함
    if checkBreak(loc_snake, loc_add):
        loc_snake.append(loc_add)
    else:
        break

    if is_true:
        loc_apple.pop(idx)
    else:
        loc_snake.pop(0)

    print('=' * 50)
    turn += 1

print(turn+1)