class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        dict_s1 = {}
        dict_s2 = {}
        len_s1 = len(s1)
        for _char in s1:
            if _char not in dict_s1:
                dict_s1[_char] = 1
            else:
                dict_s1[_char] += 1
        print(dict_s1)
        for i in range(len_s1):
            if s2[i] not in dict_s2:
                dict_s2[s2[i]] = 1
            else:
                dict_s2[s2[i]] += 1
        print(dict_s2)

        i = 0
        while i < len(s2)-len_s1+1:
            if dict_s2 == dict_s1:
                return True
            print(i)
            if i == len(s2) - len_s1:
                break
            dict_s2[s2[i]] -= 1
            print("before", dict_s2)
            if dict_s2[s2[i]] == 0:
                dict_s2.pop(s2[i])
            print("after", dict_s2)
            print(i+len_s1-1)
            i += 1
            if s2[i+len_s1-1] not in dict_s2:
                dict_s2[s2[i+len_s1-1]] = 1
            else:
                dict_s2[s2[i+len_s1-1]] += 1
        return False