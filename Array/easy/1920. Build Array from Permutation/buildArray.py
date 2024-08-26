#time complexity : O(n)
#space complexity : O(n)
class Solution(object):
    def buildArray(self, nums):
        n = len(nums)
        ans = []
        for i in range(n):
            ans.append(nums[nums[i]])
            
        return ans
    
#time complexity : O(n)
#space complexity : O(n)
class Solution(object):
    #in this solution we reserve a list with size of nums, then modify them
    def buildArray(self, nums):
        n = len(nums)
        ans = list(nums)
        for i in range(n):
            ans[i] = nums[nums[i]]
            
        return ans