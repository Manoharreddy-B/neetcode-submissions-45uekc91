class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        seq_dict = {}
        for num in nums:
            if num-1 in nums_set:
                continue
            if num not in seq_dict:
                seq_dict[num] = [num]
                temp_num = num
                while temp_num+1 in nums_set:
                    seq_dict[num].append(temp_num+1)
                    temp_num = temp_num+1

        max_len = 0
        for key,value in seq_dict.items():
            loc_len = len(value)
            if loc_len > max_len:
                max_len = loc_len
        return max_len

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         _dict = {}       # boundary -> full sequence list
#         seen = set()     # used to ignore duplicate numbers
#         max_len = 0

#         for num in nums:
#             if num in seen:
#                 continue

#             seen.add(num)

#             # Case 1: num connects a sequence on the left and a sequence on the right
#             if num - 1 in _dict and num + 1 in _dict:
#                 left_sequence = _dict[num - 1]
#                 right_sequence = _dict[num + 1]

#                 new_sequence = left_sequence + [num] + right_sequence

#                 low = new_sequence[0]
#                 high = new_sequence[-1]

#                 # num - 1 and num + 1 are now internal boundaries
#                 _dict.pop(num - 1)
#                 _dict.pop(num + 1)

#                 # Store the merged sequence at both outer boundaries
#                 _dict[low] = new_sequence
#                 _dict[high] = new_sequence

#             # Case 2: num extends a sequence from the left
#             elif num - 1 in _dict:
#                 left_sequence = _dict[num - 1]

#                 new_sequence = left_sequence + [num]

#                 low = new_sequence[0]
#                 high = new_sequence[-1]

#                 # Old right boundary becomes internal
#                 _dict.pop(num - 1)

#                 # Store at both new boundaries
#                 _dict[low] = new_sequence
#                 _dict[high] = new_sequence

#             # Case 3: num extends a sequence from the right
#             elif num + 1 in _dict:
#                 right_sequence = _dict[num + 1]

#                 new_sequence = [num] + right_sequence

#                 low = new_sequence[0]
#                 high = new_sequence[-1]

#                 # Old left boundary becomes internal
#                 _dict.pop(num + 1)

#                 # Store at both new boundaries
#                 _dict[low] = new_sequence
#                 _dict[high] = new_sequence

#             # Case 4: num does not connect to any existing sequence
#             else:
#                 new_sequence = [num]
#                 _dict[num] = new_sequence

#             max_len = max(max_len, len(new_sequence))

#         return max_len