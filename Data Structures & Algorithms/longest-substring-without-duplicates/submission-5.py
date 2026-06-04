class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        cur_set = set()
        left = 0
        answer = 0
        for right in range(len(s)):
            while left < len(s) and s[right] in cur_set:
                    left += 1
                    cur_set = set(s[left:right])
                    
            if s[right] not in cur_set:
                cur_set.add(s[right])
            
            answer = max(answer, right-left+1)
        return answer

        # output = 0
        # temp_set = set()
        # print(len(s))
        # for i in range(len(s)):
        #     print(ord(s[i]))
        #     if ord(s[i]) not in temp_set:
        #         print(ord(s[i]))
        #         temp_set.add(ord(s[i]))
        #         temp_len = len(temp_set)
        #     else:
        #         temp_set = set()
        #         temp_set.add(ord(s[i]))
        #     print(temp_len)
        #     output = max(temp_len, output)
        # return output
        # output = 0
        # temp_set = set()
        # temp_list = []
        # i = 0
        # while i < len(s):
        #     if ord(s[i]) not in temp_set:
        #         # print(ord(s[i]))
        #         temp_list.append(ord(s[i]))
        #         temp_set.add(ord(s[i]))
        #         # temp_len = len(temp_list)
        #         print(ord(s[i]), temp_list)
        #     else:
        #         while i < len(s) and ord(s[i]) in temp_set:
        #             print("else", ord(s[i]), temp_list)
        #             del temp_list[0]
        #             temp_set = set(temp_list)
        #             i += 1
            
        #     temp_len = len(temp_list)
        #     print(temp_len)
        #     output = max(temp_len, output)
        #     i += 1
        # return output

        # complex but not standard sliding window solution
        # output = 0
        # temp_set = set()
        # temp_list = []
        # i = 0
        # while i < len(s):
        #     if s[i] not in temp_set:
        #         temp_list.append(s[i])
        #         temp_set.add(s[i])
        #         i += 1
        #     else:
        #         while i < len(s) and s[i] in temp_set:
        #             removed_char = temp_list[0]
        #             del temp_list[0]
        #             temp_set.remove(removed_char)

        #         temp_list.append(s[i])
        #         temp_set.add(s[i])
        #         i += 1
            
        #     temp_len = len(temp_list)
        #     output = max(temp_len, output)
        # return output


        # standard but classic sliding window
        # left = 0 
        # output = 0
        # seen = set()

        # for right in range(len(s)):
        #     while s[right] in seen:
        #         seen.remove(s[left])
        #         left += 1
        #     seen.add(s[right])
        #     output = max(output, right-left+1)
        # return output