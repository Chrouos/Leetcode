class Solution {
public:
    bool isPalindrome(int x) {
        
        if(x < 0) return false;
        
        long long reverseX = 0;
        bool answer = true;
        
        int tempX = x;
        while(tempX){
            reverseX = (reverseX * 10) + (tempX % 10);
            tempX /= 10;
        }
        
        if( x != reverseX) answer = false;
        
        return answer;
        
    }
};