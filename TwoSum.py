class Solution(object):
    def twoSum(self, nums, target):
        result = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i]+nums[j] == target): 
                 result.append(i)
                 result.append(j)
                 return result
sol = Solution()
print(sol.twoSum([1,2,3,4,5,6,7], 5))