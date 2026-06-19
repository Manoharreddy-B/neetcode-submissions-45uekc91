class Solution:
    def findMin(self, nums: List[int]) -> int:
        # start num > mid then it is guaranteed that answer is in first half
        # start num < mid then it is guaranteed that answer is in second half

        def recMin(start, end):

            mid = (start + end)//2
            if start == end:
                return nums[start]
            if nums[start] < nums[end]:
                return nums[start]
            if nums[mid] >= nums[start]:
                return recMin(mid + 1, end)
            else:
                return recMin(start, mid)
        return recMin(0, len(nums)-1)