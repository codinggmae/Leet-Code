//time complexity : O(n^2)
//space complexity : O(1)
class Solution 
{
public:
    //in this solution i walk through the vector with nested loops and find our branch
    int numIdenticalPairs(vector<int>& nums)
    {
        int len = nums.size();
        int k = 0;
        for (int i = 0; i < len; i++)
        {
            for (int j = 0; j < len; j++)
            {
                if (nums[i] == nums[j] and i < j) k++;
            }
        }
        return k;
    }
};

//time complexity : O(n)
//space complexity : O(n)
class Solution 
{
public:
    //in this solution i walk through vector with a loop then add each element in to hash map that values are count of each element in the vector
    int numIdenticalPairs(vector<int>& nums)
    {
        unordered_map<int, int> map;
        int k = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            //when meet same key, plus it's value to k then plus one to it's value 
            if (map[nums[i]])
            {
                k += map[nums[i]];
                map[nums[i]] += 1;
            }
            //if not in dict add it and set it's count to 1
            else
            {
                map[nums[i]] = 1;
            }
        }
        return k;
    }
};