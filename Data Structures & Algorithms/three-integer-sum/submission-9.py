class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                # 1. Skip duplicates for left and right immediately
                if left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue
                if right < len(nums) - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                    continue

                # 2. Then do your normal sum checks
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return ans

# -4 -1 -1 0 1 2
#  0 1 2  3 4 5 

# -4



