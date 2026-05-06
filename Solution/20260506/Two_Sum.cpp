// Hash Map (One Pass)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> complement;
        for(int i = 0; i < nums.size(); ++i)
        {
            int diff = target - nums[i];
            if(complement.count(diff))
            {
                return {complement[diff], i};
            }
            complement[nums[i]] = i;
        }
        return {};
    }
};
