//time complexity : O(n)
//space complexity : O(n)
class Solution 
{
public:
    //in this solution i loop in the vector and append elements in to a new vectors
    vector<int> shuffle(vector<int>& nums, int n) 
    {
        vector<int> ans;
        for (int i = 0; i < n; i++)
        {
            ans.push_back(nums[i]);
            ans.push_back(nums[n + i]);
        }
        return ans;
    }
};