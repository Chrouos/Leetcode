class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int,int> dictionary;      
        for(int i=0; i<nums.size(); i++){
					
			int	match = target - nums[i];

			if(dictionary.count(match) && dictionary[match] != i)
				return {dictionary[match], i};
            
			dictionary[nums[i]] = i;
        }
        
        return {};
        
    }
};