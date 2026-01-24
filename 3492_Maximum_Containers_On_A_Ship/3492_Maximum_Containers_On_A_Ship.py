class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        output = maxWeight // w
        if output < n*n:
            return output
        else:
            return n*n