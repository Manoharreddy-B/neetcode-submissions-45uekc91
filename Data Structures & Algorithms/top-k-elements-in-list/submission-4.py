class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                count_dict[num] += 1
        
        # freq_dict = {}
        # for key, value in count_dict.items():
        #     if value in freq_dict:
        #         freq_dict[value].append(key)
        #     else:
        #         freq_dict[value] = [key]
        # freq_dict = dict(sorted(freq_dict.items()))

        # output = []
        # for key, values in reversed(freq_dict.items()):
        #     for num in values:
        #         output.append(num)
        #     if len(output) >= k:
        #         break
        # return output

        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in count_dict.items():
            freq[count].append(num)

        output = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                output.append(num)

                if len(output) == k:
                    return output