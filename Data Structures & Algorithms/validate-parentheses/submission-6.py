class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        par_pair = {')':'(','}':'{',']':'['}
        par_list = []

        for ch in s:
            if ch not in par_pair:
                par_list.append(ch)
            elif not par_list or par_list.pop() != par_pair[ch]:
                return False
    
        return not par_list