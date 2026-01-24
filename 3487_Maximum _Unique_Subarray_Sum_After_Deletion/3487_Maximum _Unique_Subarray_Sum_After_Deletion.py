class Solution:
    def maxSum(self, nums: List[int]) -> int:
        sub_array = [max(nums)]
        maximum = max(nums)
        nums.remove(max(nums))
        for i in nums:
            if i in sub_array or i+maximum<=maximum:
                continue
            else:
                sub_array.append(i)
                maximum += i
        return maximum