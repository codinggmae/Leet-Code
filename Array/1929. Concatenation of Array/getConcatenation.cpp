//time complexity : O(n)
//spcae complexity : O(n)

class Solution 
{
public:
    //in this solution i reserved a new list with size of n * 2 and initial it
    vector<int> getConcatenation(vector<int>& nums)
    {
        int n = nums.size();
        vector<int> nvecotr(n * 2);
        for (int i = 0; i < n; i++)
        {
            nvecotr[i] = nums[i];
            nvecotr[i + n] = nums[i];
        }
        return nvecotr;
    }
};