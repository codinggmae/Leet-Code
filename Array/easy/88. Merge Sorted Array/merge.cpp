//merge two vector and sort nums1
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        for (int n1 = m, n2 = 0; n2 < n; n2++, n1++) {
            nums1[n1] = nums2[n2];
        }
        sort(nums1.begin(), nums1.end());
    }
};


//time complexity : O(m+n)
//space complexity : O(1)
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int n1 = m - 1;
        int n2 = n - 1;
        int w = n + m - 1;
        //continue until we reach to nums2 size. each time in loop we decrease write index
        while (n2 >= 0) {
            //if current ith nums1 index is bigger than nums2' index write nums1' index in write' index and decrease nums2 index
            if (n1 >= 0 && nums1[n1] > nums2[n2]) {
                nums1[w--] = nums1[n1--];
            }
            //if it ins't bigger (equal or less)
            else {
                //write nums2' index in write index and decrease nums2 index
                nums1[w--] = nums2[n2--];
            }
        }
    }
};
