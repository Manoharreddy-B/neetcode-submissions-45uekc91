class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_set = set(s)
        max_len = 0
        for _char in s_set:
            j = 0
            temp_j = j
            while j <len(s):
                length = 0
                temp_k = k
                while j < len(s):
                    if s[j] != _char:
                        if temp_k == 0:
                            break
                        temp_k -=1
                    length += 1
                    j += 1
                j = temp_j + 1
                temp_j += 1
                max_len = max(max_len, length)
        return max_len