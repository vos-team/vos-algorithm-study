class Solution:
    def dailyTemperatures(self, temperatures):
        st = [(0, 101)]
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            t = temperatures[i]
            while st[-1][-1] < t:
                target_idx, lower_t = st.pop()
                answer[target_idx] = i - target_idx
            st.append((i, t))
        return answer
