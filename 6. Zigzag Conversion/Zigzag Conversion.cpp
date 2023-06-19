class Solution {
public:
    string convert(string s, int numRows) {
        string ans = "";
        // string s = "PAYPALISHIRING";
        // int numRows = 4;
        
        // get the interval of total: 
        // 1(1), 2(2), 4(3), 6(4), 8(5)
        int total_interval = (numRows - 1) * 2;
        if (total_interval == 0) total_interval = 1;
        
        int temp_interval = 0, 
            start_index = 0, temp_index = 0;
        for(int index = 0; index < s.size(); index++){
            
            ans += s[temp_index];
            
            if(temp_interval == total_interval)
                temp_interval = 0;
            
            temp_interval = total_interval - temp_interval;
            temp_index += temp_interval;
            
            
            // turn to start
            if(temp_index >= s.size()){
                start_index++;
                temp_index = start_index;
                temp_interval = (2 * start_index);
            }
            
        }
        return ans;
    }
};