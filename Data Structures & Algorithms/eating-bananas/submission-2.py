class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        min_pile = 1
        ans = float('inf')
        while max_pile >= min_pile:
            mid = (max_pile + min_pile)//2
            hours = 0
            for i in range(len(piles)):
                hours += piles[i]//mid
                if piles[i]%mid != 0:
                    hours += 1
            if hours <= h:
                ans = min(ans,mid)
                max_pile = mid - 1
            else:
                min_pile = mid + 1
        return int(ans) if ans != float('inf') else -1