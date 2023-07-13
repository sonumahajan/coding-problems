class Solution:
    def twoSum(self, nums, target):
        result = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                sum = nums[i]+nums[j]
                if(sum == target):
                    if(i != j and i not in result and j not in result):
                        result.append(i)
                        result.append(j)
        return result

obj = Solution()
# result = obj.twoSum([2,7,11,15], 9)
# result = obj.twoSum([3,2,4], 6)
result = obj.twoSum([3,3], 6)

print(result)

