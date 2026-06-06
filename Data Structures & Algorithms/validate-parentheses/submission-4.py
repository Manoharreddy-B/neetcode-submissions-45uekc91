class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
            
        par_pair = {')':'(','}':'{',']':'['}
        par_list = []

        for ch in s:
            if ch in par_pair:
                if len(par_list) > 0 and par_list[-1] == par_pair[ch]:
                    par_list.pop()
                else:
                    return False
            else:
                par_list.append(ch)

        if len(par_list) > 0:
            return False
                
        return True