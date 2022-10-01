from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures):
        st = deque()
        st.append((0, 101))
        # 스택 생성 - 기본값으로 100도 보다 높은 값을 하나 넣어둬서 절대 빠져나오지 않도록 함

        answer = [0] * len(temperatures)  # 0으로 초기화한 정답 리스트 생성

        for i in range(len(temperatures)):
            t = temperatures[i]
            while st[-1][-1] < t:  # 스택에 마지막으로 들어간 온도가 현재 온도보다 낮을 경우
                target_idx, lower_t = st.pop()  # 뽑아내서
                answer[target_idx] = (
                    i - target_idx
                )  # 현재 온도 인덱스와의 차이(=날짜차이)로 정답 리스트를 업데이트 시킴

            st.append((i, t))  # 현재 온도를 스택에 추가함
        return answer
