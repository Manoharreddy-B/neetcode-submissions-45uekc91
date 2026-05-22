class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            if num != 0:
                product *= num
                
        answer = []
        for num in nums:
            if zero_count > 1:
                answer.append(0)
            elif zero_count == 1:
                answer.append(product if num == 0 else 0)
            else:
                answer.append(product//num)
        return answer