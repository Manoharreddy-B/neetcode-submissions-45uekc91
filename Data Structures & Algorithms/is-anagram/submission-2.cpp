#include <unordered_map>
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        std::unordered_map<char, int> dict_s;
        std::unordered_map<char, int> dict_t;

        for (char char_s: s) {
            if (dict_s.find(char_s) == dict_s.end()) {
                dict_s[char_s] = 1;
            } else {
                dict_s[char_s] += 1;
            }
        }

        for (char char_t: t) {
            if (dict_t.find(char_t) == dict_t.end()) {
                dict_t[char_t] = 1;
            } else {
                dict_t[char_t] += 1;
            }
        }

        for (auto const& [key, val] : dict_s) {
            if (dict_t.find(key) == dict_t.end() || dict_t[key] != val){
                return false;
            }
        }

        return true;
    }
};