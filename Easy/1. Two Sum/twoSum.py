class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        searchDict = {}
        for i in range(len(nums)):
            cmp = target - nums[i]
            if cmp in searchDict:
                return [searchDict[cmp], i]
            
            searchDict[nums[i]] = i
            
        return []