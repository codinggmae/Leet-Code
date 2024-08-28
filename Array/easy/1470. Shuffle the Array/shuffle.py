#time complexity : O(n)
#space complexity : O(n)
class Solution(object):
    #in this solution i loop in the list and append elements in to a new list
    def shuffle(self, nums, n):
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[n+i])
                
        return ans