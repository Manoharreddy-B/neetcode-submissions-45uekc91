class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_count = [0]*26
        s2_count = [0]*26

        m = len(s1)

        for ch in s1:
            s1_count[ord(ch) - ord('a')] += 1

        for right in range(len(s2)):
            s2_count[ord(s2[right])-ord('a')] += 1

            if right >= m:
                s2_count[ord(s2[right-m])-ord('a')] -= 1
            
            if s1_count == s2_count:
                return True
        return False