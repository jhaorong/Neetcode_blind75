//Hash Table with valid key
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> group_map;
        for(auto str : strs)
        {
            vector<int> count(26, 0);
            for(char c : str)
            {
                count[c - 'a']++;
            }
            string key = to_string(count[0]);
            for(int i = 1; i < 26; ++i)
            {
                key += ',' + to_string(count[i]);
            }
            group_map[key].push_back(str);
        }
        vector<vector<string>> group_vector;
        for(auto pair : group_map)
        {
            group_vector.push_back(pair.second);
        }
        return group_vector;
    }
};