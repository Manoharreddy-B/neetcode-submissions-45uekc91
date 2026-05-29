class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        for _char in s:
            if _char.isalnum():
                clean_s += _char.lower()
        length = len(clean_s)
        if length == 1 or length == 0:
            return True
        if length % 2 == 0:
            half = length//2
        else:
            half = length//2 + 1
        i = 0
        while i <= half :
            if clean_s[i] == clean_s[length-i-1]:
                i += 1
                continue
            else:
                return False
        return True