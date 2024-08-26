//time complexity : O(n)
//space complexity : O(1)
class Solution
{
public:
    //in this solution i loop in list and find my branch
    int minimumOperations(vector<int>& nums) 
    {
        int operations = 0;
        for (int i : nums)
        {
            //in reminder of each elemebt only 1 and 2 will make a number divide able to 3
            if (i % 3 == 1 or i % 3 == 2) operations++;
        }
        return operations;
    }
};

//time complexity : O(n)
//space complexity : O(1)
class Solution
{
public:
    //more compact branch
    int minimumOperations(vector<int>& nums)
    {
        int operations = 0;
        for (int i : nums)
        {
            if (i % 3 != 0) operations++;
        }
        return operations;
    }
};