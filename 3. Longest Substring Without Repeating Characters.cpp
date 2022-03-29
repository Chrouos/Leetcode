class Solution {
   public:
    int lengthOfLongestSubstring(string s) {
        // 做到不重複已出現過字母？

        int size = s.length(), maxSize = 0;
        vector<char> answer;

        for (int i = 0; i < size; i++) {
            // answer.push_back(s[i]);
            vector<char>::iterator it =
                find(answer.begin(), answer.end(), s[i]);
            int deleSize = 0;
            if (it != answer.end()) {
                deleSize = distance(answer.begin(), it);
                answer.erase(answer.begin(), answer.begin() + deleSize + 1);
            }

            answer.push_back(s[i]);
            if (answer.size() > maxSize)
                maxSize = answer.size();
        }

        return maxSize;
    }
};