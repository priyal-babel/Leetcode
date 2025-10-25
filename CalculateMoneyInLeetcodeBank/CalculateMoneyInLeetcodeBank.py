class Solution:
    def totalMoney(self, n: int) -> int:
        totalMoney = 0
        day = 1
        for i in range(1,n+1):
            totalMoney += day
            if i % 7 == 0:
                day = i // 7
            day += 1

        return totalMoney