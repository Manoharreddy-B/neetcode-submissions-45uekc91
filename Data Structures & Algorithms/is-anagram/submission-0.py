class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}
        for char_s in s:
            if char_s not in dict_s:
                dict_s[char_s] = 1
            else:
                dict_s[char_s] += 1
        for char_t in t:
            if char_t not in dict_t:
                dict_t[char_t] = 1
            else:
                dict_t[char_t] += 1
        for item_s in dict_s:
            if item_s not in dict_t or dict_s[item_s] != dict_t[item_s]:
                return False
        return True