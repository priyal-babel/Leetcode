class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        num_dict = {}
        for i in range(len(nums)):
            if nums[i] in num_dict:
                num_dict[nums[i]] += 1
            else:
                num_dict[nums[i]] = 1
        maximum = max(num_dict.values())
        count = 0
        for key,values in num_dict.items():
            if values == maximum:
                count += values
            else:
                continue
        return count
        