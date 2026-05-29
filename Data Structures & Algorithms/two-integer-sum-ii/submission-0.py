class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        
        for i, num in enumerate(numbers):
            find_num = target - num
            left = i + 1
            right = length - 1
            while left<= right:
                mid = left + (right - left) // 2
                if numbers[mid] == find_num:
                    return [i + 1, mid + 1]
                elif numbers[mid] < find_num:
                    left = mid + 1
                else:
                    right = mid - 1
