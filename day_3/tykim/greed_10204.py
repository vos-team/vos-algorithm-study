# 문자열 s와 t를 받음
s = list(input())
t = list(input())

def matched(t):
    # 문자열이 같으면 출력 후 종류
    if s == t:
        print(1)
        return
    # 문자열이 다르면 주어진 규칙에 따라 재귀 진행
    elif s != t:
        if len(t) == 0:
            print(0)
            return
        elif t[-1] == "A":
            t.pop()
            matched(t)
        elif t[-1] == "B":
            t.pop()
            t = t[::-1]
            matched(t)
matched(t)
