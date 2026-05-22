class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            if num != 0:
                product *= num
            elif zero_count > 1:
                product = 0
                
        answer = []
        for num in nums:
            if num != 0 and zero_count >= 1:
                answer.append(0)
            elif num == 0:
                answer.append(product)
            else:
                answer.append(int(product/num))
        return answer