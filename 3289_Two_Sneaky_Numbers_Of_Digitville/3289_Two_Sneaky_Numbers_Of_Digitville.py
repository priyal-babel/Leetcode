class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        num_dict = {}
        final_arr = []
        for i in range(len(nums)):
            if nums[i] in num_dict:
                final_arr.append(nums[i])
            else:
                num_dict[nums[i]] = 1
        return final_arr
        