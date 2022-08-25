#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]  #since result is in an array
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):  #j is from i+1 since i is covered in prev loop
                if nums[i]+nums[j]==target:  # to check if it is equal to target
                    result.append(i)
                    result.append(j)
                    
        return result
        
        
        # [2,7,11,15]  9
        
        
