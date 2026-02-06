class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        placed = []
        for i in fruits:
            j = 0
            while j< len(baskets):
                if i <= baskets[j]:
                    baskets.pop(j)
                    placed.append(i)
                    break
                else:
                    j += 1
        return len(fruits) - len(placed)
        