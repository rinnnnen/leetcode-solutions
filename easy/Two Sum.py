class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)): # go on every num
            for j in range(i + 1, len(nums)): # find second numb after upper
                if nums[i] + nums[j] == target:
                    return [i,j]
