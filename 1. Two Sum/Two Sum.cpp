class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int,int> dictionary;      
        for(int i=0; i<nums.size(); i++){
					

			if(dictionary.count(target - nums[i]) && dictionary[target - nums[i]] != i)
				return {dictionary[target - nums[i]], i};
            
			dictionary[nums[i]] = i;
        }
        
        return {};
        
    }
};