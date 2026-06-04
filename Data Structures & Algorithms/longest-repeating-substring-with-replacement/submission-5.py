class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        answer = 0 
        count_dict = {}
        if len(s) == 0:
            return 0

        for right in range(len(s)):
            window_size = right - left + 1
            max_freq = 0
            if s[right] not in count_dict:
                count_dict[s[right]] = 1
            else:
                count_dict[s[right]] += 1
            for key, value in count_dict.items():
                    max_freq = max(max_freq, value)

            while window_size - max_freq > k:
                count_dict[s[left]] -= 1
                if count_dict[s[left]] == 0:
                    count_dict.pop(s[left])
                left += 1
                window_size = right - left + 1

                # calculate new max freq
                for key, value in count_dict.items():
                    max_freq = max(max_freq, value)

            answer = max(answer, window_size)
        return answer



        # s_set = set(s)
        # max_len = 0
        # for _char in s_set:
        #     j = 0
        #     temp_j = j
        #     while j <len(s):
        #         length = 0
        #         temp_k = k
        #         while j < len(s):
        #             if s[j] != _char:
        #                 if temp_k == 0:
        #                     break
        #                 temp_k -=1
        #             length += 1
        #             j += 1
        #         j = temp_j + 1
        #         temp_j += 1
        #         max_len = max(max_len, length)
        # return max_len