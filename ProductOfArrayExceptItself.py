#asked in VMware
#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

#You must write an algorithm that runs in O(n) time and without using the division operation.
#Good example of of getting data from left side and right side

# how i came up, i was thinknig to store result, but that subresult i need from both side, left side and right side
# that is how i came up with this approach

#Time-complexity: o(n) and space-complexiy: o(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1 for ele in nums]
        right = [1 for ele in nums]
        
        for i in range(1, len(nums)):
            left[i] = nums[i-1] * left[i-1]
        
        for i in range(len(nums) - 2, -1, -1):
            right[i] = nums[i+1] * right[i+1]
            
        print("left array is", left)
        print("right array is", right)
        #we will get res by multiplying both side for index
            
        for i in range(len(nums)):
            nums[i] = left[i] * right[i]
            
        return nums
        