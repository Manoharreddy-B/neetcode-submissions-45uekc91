class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_a = set()
        for num in nums:
            if num not in set_a:
                set_a.add(num)
            else:
                return True
        return False
        