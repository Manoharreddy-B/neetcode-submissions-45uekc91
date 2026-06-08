class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []
        for i in range(len(temperatures)):
            j = i + 1
            while j< len(temperatures) and temperatures[i] >= temperatures[j]:
                j += 1
            if i == len(temperatures)-1:
                answer.append(0)
            elif j< len(temperatures) and temperatures[i] < temperatures[j]:
                answer.append(j-i)
            else: 
                answer.append(0)

        return answer