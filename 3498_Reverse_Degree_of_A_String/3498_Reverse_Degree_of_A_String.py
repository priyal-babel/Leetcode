class Solution:
    def reverseDegree(self, s: str) -> int:
        string = 'abcdefghijklmnopqrstuvwxyz'
        reverse_string = string[::-1]
        final_sum = 0
        for i in range(len(s)):
            final_sum += (i+1)*(reverse_string.index(s[i])+1)
        return final_sum     