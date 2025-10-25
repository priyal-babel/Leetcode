class Solution:
    def totalMoney(self, n: int) -> int:
        remainder = n % 7
        quotient = n // 7
        tempSum = remainder*(remainder+1)/2
        if quotient > 0:
            tempSum += 28*quotient + 7 * quotient*(quotient-1)/2 + (quotient * remainder)
        return int(tempSum)