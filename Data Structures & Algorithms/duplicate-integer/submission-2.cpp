#include <set>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> mySet;
        for (int num: nums) {
            if (!mySet.contains(num)){
                mySet.insert(num);
            } else {
                return true;
            }
        }
        return false;
    }
};