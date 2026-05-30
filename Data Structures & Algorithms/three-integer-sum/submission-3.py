class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def helperTwoSum(left, right, sorted_nums, j):
            temp_answer = []
            while left < right:
                target = - sorted_nums[left] - sorted_nums[right]
                if target == sorted_nums[j-1]:
                    temp_answer.append([sorted_nums[j-1], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
                elif target > sorted_nums[j-1]:
                    left += 1
                else:
                    right -= 1
            return temp_answer
                
        sorted_nums = sorted(nums)
        length = len(nums)
        seen = set()
        answer = []
        for j in range(length, 0, -1):
            left = 0
            right = j - 2
            output = helperTwoSum(left, right, sorted_nums, j)
            if output != None:
                for lis in output:
                    output_tuple = tuple(sorted(lis))
                    if output_tuple not in seen:
                        seen.add(output_tuple)
                        answer.append(lis)
        return answer
        