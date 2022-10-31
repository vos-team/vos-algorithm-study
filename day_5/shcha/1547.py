N = int(input())

cups = [1,2,3]
for _ in range(N):
    x, y = map(int, input().split())
    
    xi = cups.index(x) # 컵의 번호 = 인덱스  
    yi = cups.index(y) # 컵의 번호 = 인덱스
    
    cups[xi], cups[yi] = cups[yi], cups[xi] #컵의 위치를 바꿔줌

    # print(cups) #변경되는 컵의 번호 확인해보기
    
print(cups[0]) #공의 위치는 항상 첫번째에 위치! 이때의 컵 번호는?
