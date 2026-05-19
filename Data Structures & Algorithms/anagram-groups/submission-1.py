class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash_map = {}
        # for word in strs:
        #     sorted_word_list = sorted(word)
        #     sorted_word = ""
        #     for letter in sorted_word_list:
        #         sorted_word += letter
        #     if sorted_word not in hash_map:
        #         hash_map[sorted_word] = [word]
        #     else:
        #         hash_map[sorted_word].append(word)
        # output = []
        # for sorted_word in hash_map:
        #     output.append(hash_map[sorted_word])
        # return output

        result = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(word)
        return list(result.values())