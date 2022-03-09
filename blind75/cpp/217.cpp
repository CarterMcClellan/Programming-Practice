class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for(int i = 0; i < nums.size(); i++)
            seen.insert(nums[i]);
        return seen.size() != nums.size();
    }
};
