class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        int start = 0, end = 0, max = 0;
        unordered_map <char, int> tempList;
        for(int i = 0; i < s.length(); i++) {

            // if repeated, change number: end, last answer is end - start;
            if(tempList.count(s[i]) > 0 && tempList[s[i]] >= start) {
    //			cout << tempList[s[i]] <<endl;

                start = tempList[s[i]];
                end = i;
                max = (max < end - start ) ? end - start : max;
            }
            
            else if ( end == 0) max++;
            
            else if ( i - start > max) max = i - start;

            tempList[s[i]] = i;
        }
        return max;
	
    }
};