//time complexity: O(n)
//space complexity: O(1)
class Solution
{
public:
    int removeElement(vector<int>& nums, int val)
    {
        for (int i = 0; i < nums.size();)
        {
            if (nums[i] == val)
            {
                nums.erase(nums.begin() + i); // Erase element at index i
            }
            else
            {
                // Only increment if no element is erased
                i++; 
            }
        }
        //only we have unique value in nums so we can return num's len
        return nums.size();
    }
};

//time complexity: O(n)
//space complexity: O(1) 
class Solution
{
public:
    //two pointer method
    int removeElement(vector<int>& nums, int val)
    {
        int iw = 0;
        for (int ir = 0; ir < nums.size(); ir++)
        {
            //if that value is not same as val replca iw with ir
            if (nums[ir] != nums[iw])
            {
                nums[iw] = nums[ir];
                iw++;
            }
        }
        //iw changes when we find a non val in nums so we can return it as answer
        return iw;
    }
};