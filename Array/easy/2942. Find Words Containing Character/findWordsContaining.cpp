//time complexity : O(n)
//space complecity : O(n)
class Solution 
{
public:
    //in this solution i loop in the vector and look for branch
    vector<int> findWordsContaining(vector<string>& words, char x) 
    {
        vector<int> ans;
        for (int i = 0; i < words.size(); i++)
        {
            
            //when branch is true add index to the answer vector
            if (words[i].find(x) != string::npos) ans.push_back(i);
        }
        return ans;
    }
};