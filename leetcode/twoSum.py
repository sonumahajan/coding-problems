# class Solution:
def twoSum(nums, target):
    result = []
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            sum = nums[i]+nums[j]
            if(sum == target):
                if(i != j and i not in result and j not in result):
                    result.append(i)
                    result.append(j)
    return result

# Solution s1 = object Solution()
print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))

