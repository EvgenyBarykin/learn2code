# variant 1
'''class Solution(object):
    def search(self, nums: list[int], target: int) -> int:
        if target in nums:
            return (nums.index(target))
        else:
            return -1
'''
nums = [5]
target = 5


'''Sol=Solution()
result=Sol.search(nums,target)
print(result)'''

# variant 2
'''class Solution(object):
    def search(self, nums, target):
        index = -1
        for i, num in enumerate(nums):
            if num == target:
                index = i
                break
        return index

Sol=Solution()
result=Sol.search(nums,target)
print(result)'''

# variant 3


class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        while (right >= left):
            center_idx = left + (right-left)//2
            if nums[center_idx] == target:
                return center_idx
            elif nums[center_idx] < target:
                left = center_idx + 1
            else:
                right = center_idx - 1
# if nothing was found
        return -1


Sol = Solution()
result = Sol.search(nums, target)
print(result)
