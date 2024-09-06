#time complexity: O(n)
#space complexity: O(1)
class Solution(object):
    #pop each element that contain val
    def removeElement(self, nums, val):
        #start index: len(nums), stop index: -1(for complete deletion), step: each time: -1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        #only we have unique value in nums so we can return num's len
        return len(nums)
                
#time complexity: O(n)
#space complexity: O(1)        
class Solution(object):
    #two pointer method
    def removeElement(self, nums, val):
        iw = 0
        for ir in range(len(nums)):
            #if that value is not same as val replca iw with ir 
            if nums[ir] != val:
                nums[iw] = nums[ir]
                iw+=1
        #iw changes when we find a non val in nums so we can return it as answer
        return iw