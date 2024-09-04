#time complexity: O(n)
#space complexity: O(1)
class Solution(object):
    #two pointer method
    def removeDuplicates(self, nums):
        #write index
        iw = 0
        #read index each time will increase
        for ir in range(len(nums)):
            if nums[ir] != nums[iw]:
                #move write index forward
                iw += 1
                nums[iw] = nums[ir]
        #we start write index from zero when so we need to add one to it. imagine we have nums with len 2 and 2 elements are same we need to return 1 (not 0)
        return iw+1