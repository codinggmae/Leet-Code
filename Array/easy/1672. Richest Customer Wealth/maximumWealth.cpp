//time complexity : O(n+m)
//space complexity : O(1)
class Solution 
{
public:
    //in this solution i loop in the 2dvector and sum all elements in that index and find the max index
    int maximumWealth(vector<vector<int>>& accounts) 
    {
        int max = 0;
        for (vector<int> i : accounts)
        {
            int moneywealth = 0;
            for (int j : i)
            {
                moneywealth += j;
            }
            if (moneywealth > max)
            {
                max = moneywealth;
            }
        }
        return max;
    }
};