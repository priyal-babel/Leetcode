class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        if not nums:
            return 0
        max_len = 0
        for num in nums:
            if num - 1 not in nums:
                cur = num
                length = 1
                while cur + 1 in nums:
                    cur += 1
                    length += 1
                if length > max_len:
                    max_len = length
        return max_len
