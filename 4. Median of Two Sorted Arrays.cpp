class Solution {
   public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // 將 num2 插入 num1 中
        for (int i = 0; i < nums2.size(); i++) {
            nums1.push_back(nums2[i]);
        }
        sort(nums1.begin(), nums1.end());

        // 有中間值
        if (nums1.size() % 2 == 1)
            return nums1[(nums1.size() / 2)];
        else {
            int n = nums1.size() / 2;
            double ans = (nums1[n - 1] + nums1[n]) * 1.0 / 2;
            return ans;
        }
    }
};