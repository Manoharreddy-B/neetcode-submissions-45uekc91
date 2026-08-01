class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # seen = [0]*len(nums)

        # for num in nums:
        #     if seen[num-1]==-1:
        #         return num
        #     else:
        #         seen[num-1]=-1
        slow = 0 
        fast = 0 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow