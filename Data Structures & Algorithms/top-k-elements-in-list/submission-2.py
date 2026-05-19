from collections import OrderedDict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            if num not in count_dict:
                count_dict[num] = 1
            else:
                count_dict[num] += 1
        # print(count_dict)
        
        ord_dict = OrderedDict()
        # for key,values in count_dict.values:
        for key, value in count_dict.items():
            if value in ord_dict:
                ord_dict[value].append(key)
            else:
                ord_dict[value] = [key]
        # print(ord_dict)
        ord_dict = dict(sorted(ord_dict.items()))
        # print(ord_dict)
        # i = 1
        output = []
        for key, values in reversed(ord_dict.items()):
            # print(key, values)
            for num in values:
                output.append(num)
            if len(output) >= k:
                break
            # i += 1
        return output