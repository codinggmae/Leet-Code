#time complexity : O(n^2)
#space complexity : O(1)
class Solution(object):
    #in this solution i walk through the list with nested loops and find our branch
    def numIdenticalPairs(self, nums):
        n = len(nums)
        k = 0
        for i in range(n):
            for j in range(n):
                if i < j and nums[i] == nums[j]:
                    k += 1
                    
        return k
    
#time complexity : O(n)
#space complexity : O(n)
class Solution(object):
    #in this solution i walk through list with a loop then add each element in to dict that values are count of each element in the list
    def numIdenticalPairs(self, nums):
        dictionary = {}
        k = 0
        for i in nums:
            #when meet same key, plus it's value to k then plus one to it's value 
            if i in dictionary:
                k += dictionary[i]
                dictionary[i] += 1
            #if not in dict add it and set it's count to 1
            else:
                dictionary[i] = 1
            
        return k
