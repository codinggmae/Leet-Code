//time complexity: O(n)
//space complexity: O(1)
class Solution 
{
public:
    //two pointer method
    int removeDuplicates(vector<int>& nums) 
    {
        //write index
        int iw = 0;
        //read index each time will increase
        for (int ir = 1; ir < nums.size(); ++ir)
        {
            if (nums[ir] != nums[iw])
            {
                //move write index forward
                iw++;
                nums[iw] = nums[ir];
            }
        }
        //we start write index from zero when so we need to add one to it. imagine we have nums with len 2 and 2 elements are same we need to return 1 (not 0)
        return iw + 1;
    }
};