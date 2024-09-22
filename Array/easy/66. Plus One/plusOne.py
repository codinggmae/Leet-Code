#time complexity : O(n)
#space complexiy : O(n)
class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            #if ith digit is 9 change it to 0
            if digits[i] == 9:
                digits[i] = 0
            #if it isn't 9 just sum with 1 and return answer
            else:
                digits[i] += 1
                return digits
        # return a new list that first index is 1. because other indexes was 9
        return [1] + digits
    
    
#pythonic solution
class Solution(object):
    def plusOne(self, digits):
        #change list to an int
        num = int("".join(map(str, digits)))
        #sum with 1
        num += 1
        #change int to a list
        answer = [int(i) for i in str(num)]
        return answer