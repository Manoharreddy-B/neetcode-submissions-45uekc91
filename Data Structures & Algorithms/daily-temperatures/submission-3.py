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
        
        for i in range(len(temperatures)):
            index = 0
            while len(stack) and temperatures[i] > stack[-1][0]:
                temp = stack.pop()
                num = temp[0]
                j = temp[1]
                index += 1
                answer[j] = i-j
                           
            stack.append((temperatures[i], i))
        return answer