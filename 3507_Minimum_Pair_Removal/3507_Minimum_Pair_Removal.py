class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        sum_arr = []
        for i in range(len(nums)-1):
            sum_arr.append(nums[i] + nums[i+1])
        while True:
            print(nums)
            if nums == sorted(nums):
                return count
            else:
                count+=1
                val = min(sum_arr)
                indx = sum_arr.index(val)
                if indx != 0:
                    sum_arr[indx-1] += nums[indx+1]
                if indx != len(sum_arr)-1:
                    sum_arr[indx+1] += nums[indx]
                sum_arr.pop(indx)
                nums.pop(indx)
                nums.pop(indx)
                nums.insert(indx,val)