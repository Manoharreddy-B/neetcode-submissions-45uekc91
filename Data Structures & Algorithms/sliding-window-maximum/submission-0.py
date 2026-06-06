class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        for i in range(len(nums)-k+1):
            max_num = sorted(nums[i:i+k])[k-1]
            answer.append(max_num)
        return answer