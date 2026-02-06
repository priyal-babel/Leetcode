class Solution:
    def countMonobit(self, n: int) -> int:
        count = 1
        i = 1
        while True:
            if (2**i - 1) <= n:
                count += 1
            else:
                break
            i=i+1
        return count