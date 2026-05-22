class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product = 1
        # zero_count = 0
        # for num in nums:
        #     if num == 0:
        #         zero_count += 1
        #     if num != 0:
        #         product *= num
        #     elif zero_count > 1:
        #         product = 0
                
        # answer = []
        # for num in nums:
        #     if num != 0 and zero_count >= 1:
        #         answer.append(0)
        #     elif num == 0:
        #         answer.append(product)
        #     else:
        #         answer.append(product//num)
        # return answer


        # pre-fix and sufix product approach
        n = len(nums)
        answer = [1] * n

        prefix_product = 1

        for i in range(n):
            answer[i] = prefix_product
            prefix_product *= nums[i]
        
        suffix_product = 1

        for i in range(n - 1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]

        return answer