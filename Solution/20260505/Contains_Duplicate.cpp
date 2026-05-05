//Hash Set
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> my_set;
        for(int i=0;i<nums.size();i++)
        {
            if(my_set.find(nums[i]) != my_set.end())
            {
                return true;
            }
            my_set.insert(nums[i]);
        }
        return false;
    }
};