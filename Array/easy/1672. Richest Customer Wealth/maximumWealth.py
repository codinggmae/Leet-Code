#time complexity : O(n)
#spce complexity : O(1)
class Solution(object):
    #in this solution i loop in the list and sum all elements in that index and find the max index
    def maximumWealth(self, accounts):
        max = 0
        for i in accounts:
            money = sum(i)
            if money > max:
                max = money
                
        return max