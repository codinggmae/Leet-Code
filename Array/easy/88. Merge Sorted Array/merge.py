class Solution(object):
    def merge(self, nums1, m, nums2, n):
        #merge 2 lists and sort nums1
        nums1[:m] = nums2
        nums1.sort()

#time complexity : O(m+n)
#space complexity : O(1)
class Solution(object):
    #two pointer method
    def merge(self, nums1, m, nums2, n):
    #start from back of nums2
        n1 = m-1
        n2 = n-1
        w = n+m-1
        #continue until we reach to nums2 size
        while n2 >= 0:
            #if current ith nums2 index is bigger than nums1' index write nums2' index in write' index
            if nums1[n1] < nums2[n2]:
                nums1[w] = nums2[n2]
                #decrease nums2 index
                n2 -= 1
            #if it ins't bigger (equal or less)
            else:
                #write nums1' index in write index
                nums1[w] = nums1[n1]
                #decrease nums1 index
                n1 -= 1
            
            #each time in loop decrease write index
            w -= 1
