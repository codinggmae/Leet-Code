#time complexity : O(n)
#space complexity : O(1)
class Solution(object):
    #in this solution i loop in list and find my branch
    def minimumOperations(self, nums):
        operations = 0
        for i in nums:
            #in reminder of each elemebt only 1 and 2 will make a number divide able to 3
            if i % 3 == 1 or i % 3 == 2:
                operations += 1
                
        return operations
    
#time complexity : O(n)
#space complexity : O(1)
class Solution(object):
    def minimumOperations(self, nums):
        operations = 0
        for i in nums:
            #this is more compact branch
            if i % 3 != 0:
                operations += 1
                
        return operations