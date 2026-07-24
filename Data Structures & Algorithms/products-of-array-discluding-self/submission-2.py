class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)

        # left multiple
        left_multiple = 1
        for i in range(0, len(nums)):
            result[i] = left_multiple
            left_multiple *= nums[i]
        
        # right multiple
        right_multiple = 1
        for i in range(len(nums)-1,-1,-1):
            result[i]*=right_multiple
            right_multiple*=nums[i]
        
        return result