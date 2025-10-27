class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        multiplier1, multiplier2 = 0, 0
        number_of_lasers = 0
        for i in range(len(bank)):
            multiplier1 = bank[i].count('1')
            if multiplier1 == 0:
                continue
            number_of_lasers += multiplier1 * multiplier2
            multiplier2 = multiplier1
        return number_of_lasers