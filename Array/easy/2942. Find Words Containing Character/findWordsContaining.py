#time complexity : O(n)
#space complecity : O(n)
class Solution(object):
    #in this solution i loop in the list and look for branch
    def findWordsContaining(self, words, x):
        ans = []
        for i in range(len(words)):
            if x in words[i]:
                #when branch is true add index to the answer list
                ans.append(i)
                
        return ans