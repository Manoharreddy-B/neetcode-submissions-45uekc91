class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # answer = []
        # for i in range(len(temperatures)):
        #     j = i + 1
        #     while j< len(temperatures) and temperatures[i] >= temperatures[j]:
        #         j += 1
        #     if j< len(temperatures) and temperatures[i] < temperatures[j]:
        #         answer.append(j-i)
        #     else: 
        #         answer.append(0)
        # return answer

        answer = [0]*len(temperatures)
        stack = []
        
        for i,t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                index = stack.pop()
                answer[index] = i - index
                           
            stack.append(i)
        return answer