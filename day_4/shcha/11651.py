num = int(input())
a = []
for i in range(num):
    [x, y] = map(int, input().split()) #입력 받은 숫자의 횟수 만큼, x,y좌표를 리스트의 형태로 입력받는다.
    rev = [y, x] #xy를 뒤집은 리스트를 만들어준다
    a.append(rev)
b = sorted(a)

for i in range(num):
    print(b[i][1], b[i][0]) # 저장은 yx 으로 되어있었으므로 출력은 다시 반대로!
