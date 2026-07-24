class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        for i in range(len(nums)):
            
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = nums[left] + nums[right] + nums[i]
                if s == 0:
                    ans.append([nums[left], nums[right], nums[i]])
                    left +=1
                    right -=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right -=1
                elif s < 0:
                    left+=1
                else:
                    right-=1

        return ans


# -2 0 0 2 2