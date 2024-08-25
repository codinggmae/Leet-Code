//time complexity : O(n ^ 2)
//space complexity : O(1)
class Solution 
{
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        //in this solution we calculate complement of each element and search it in vector
        int len = nums.size();
        for (int i = 0; i < len; i++)
        {
            //find complement
            int complement = target - nums[i];
            for (int j = 0; j < len; j++)
            {
                //our result must be a vector of different indexes so i say when i and j is not equal then return vector
                if (complement == nums[j] && i != j)
                {
                    return { i, j };
                }
            }
        }   
        //if can't file answer return an empty list
        return{};
    }
};




//time complexity : O(n)
//space complexity : O(n)
class Solution 
{
public:
    //in this solution we calculate complement of each element and add it to a unordered map(dictionary) and search it in dictionary
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        unordered_map<int, int> answer {};
        for (int i = 0; i < nums.size(); i++)
        {
            //find complement
            int complement = target - nums[i];
            //if complement is in the dictionary return answer else add that num(key) and index(value) to dictionary
            if (answer.find(complement) != answer.end())
            {
                return { answer[complement], i };
            }
            else
            {
                answer[nums[i]] = i;
            }
        }
        //if can't file answer return an empty vector
        return {};
    }
};