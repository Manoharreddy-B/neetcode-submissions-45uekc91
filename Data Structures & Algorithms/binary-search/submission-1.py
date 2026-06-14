class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # while loop
        # start = 0
        # last = len(nums) - 1
        # while start <= last:
        #     mid = (start + last)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target:
        #         last = mid - 1
        #     elif nums[mid] < target:
        #         start = mid + 1
        # return -1

        # recursion

        def rec(start,last):
            if start > last:
                return -1
            mid = (start + last)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return rec(start, mid - 1)
            elif nums[mid] < target:
                return rec(mid + 1,last)
        
        return rec(0, len(nums)-1)