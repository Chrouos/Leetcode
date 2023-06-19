class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        
        int s = 0, e = 0;
        for(int n1 = 0, n2 = 0; n1 + n2 < (nums1.size() + nums2.size()) / 2 + 1 ;){
            
            if (n1 < nums1.size() ){
                if(nums1[n1] <= nums2[n2] ){
                    s = e;
                    e = nums1[n1];
                    n1++;
                }

            }
            else if (n2 < nums2.size() ){
                if (nums1[n1] > nums2[n2]){
                    s = e;
                    e = nums2[n2];
                    n2++;
                }
            }
        }

        if (((nums1.size() + nums2.size()) ) % 2 == 0)
            return (s+e) * 1.0 / 2;
        else
            return e;
        
    }
};