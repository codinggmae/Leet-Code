#time complexity : O(n^2)
#space complexity : O(1)
class Solution(object):
    #in this solution we calculate complement of each element and search it in list 
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            #find complement
            complement = target - nums[i]
            for j in range(len(nums)):
                #our result must be a list of different indexes so i say when i and j is not equal then return list
                if nums[j] == complement and i != j:
                    return [i,j]
        #if can't file answer return an empty list
        return []
                
                
#time complexity : O(n)
#space complexity : O(n)
class Solution(object):
    #in this solution we calculate complement of each element and add it to a dictionary and search it in dictionary
    def twoSum(self, nums, target):
        dictionary = {}
        for i,num in enumerate(nums):
            #find complement
            complement = target - num
            #if complement is in the dictionary return answer else add that num(key) and index(value) to dictionary
            if complement in dictionary:
                return [dictionary[complement], i]
            else:
                dictionary[num] = i
        #if can't file answer return an empty list
        return []