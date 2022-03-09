class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // hash map
        unordered_map<int, int> seenNums;
        for (int idx = 0; idx < nums.size(); idx++)
        {
            // check if element is in hash map
            if (seenNums.find(target - nums[idx]) != seenNums.end())
            {
                return {seenNums[target - nums[idx]], idx};
            }
            else 
            {
                seenNums[nums[idx]] = idx;
            }
                
            
        }
        return {0, 0};
    }
};
