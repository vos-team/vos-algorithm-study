import sys
sys.stdin = open('day_4/mjjo/2750.txt')

input = sys.stdin.readline
N = int(input())
# for _ in sorted([int(input()) for _ in range(N)]):
arr = [int(input()) for _ in range(N)]
arr.sort()
for _ in arr:
    print(_) 

# sort 함수는 리스트명.sort( ) 형식으로 "리스트형의 메소드"이며 리스트 원본값을 직접 수정합니다.
# sorted 함수는 sorted( 리스트명 ) 형식으로 "내장 함수"이며 리스트 원본 값은 그대로이고 정렬 값을 반환합니다.