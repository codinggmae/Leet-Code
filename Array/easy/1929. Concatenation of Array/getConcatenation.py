#time complexity : O(n)
#spcae complexity : O(n)
class Solution(object):
    #in this solution i reserved a new list with size of n * 2 and initial it
    def getConcatenation(self, nums):
        n = len(nums)
        #reserve new list with size n * 2 and intial each index with 0
        nlist = [0] * (n*2)
        for i in range(n):
            nlist[i] = nums[i]
            nlist[i+n] = nums[i]
            
        return nlist
    
    
#time complexity : O(n)
#spcae complexity : O(n)
class Solution(object):
    #in this solution i duplicate old list and return new list with size of n * 2 (this is benefit of python)
    def getConcatenation(self, nums):
        return nums * 2
    