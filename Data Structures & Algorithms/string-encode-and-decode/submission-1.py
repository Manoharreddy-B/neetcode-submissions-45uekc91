class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string = encoded_string + str(len(word)) + "#" + word
        # print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        while i < len(s):
            word = ""
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            length = int(length)
            # print(length, i)
            for character in s[i+1:i + length +1]:
                # print(character)
                word += character
            # i = i + int(s[i]) + 2
            i = i + length + 1
            decoded_list.append(word)
        return decoded_list