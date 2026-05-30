class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # length = len(numbers)
        
        # for i, num in enumerate(numbers):
        #     find_num = target - num
        #     left = i + 1
        #     right = length - 1
        #     while left<= right:
        #         mid = left + (right - left) // 2
        #         if numbers[mid] == find_num:
        #             return [i + 1, mid + 1]
        #         elif numbers[mid] < find_num:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        length = len(numbers)
        if length < 2:
            return []
        left = 0 
        right = length - 1
        while left < right:
            find_num = target - numbers[left]
            if find_num == numbers[right]:
                return [left+1, right+1]
            elif find_num < numbers[right]:
                right -= 1
            else:
                left += 1
