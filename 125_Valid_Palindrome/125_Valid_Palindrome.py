import math

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean_s = ''
        for i in s:
            if i.isalnum():
                clean_s += i
        for i in range(math.ceil(len(clean_s)/2)):
            if clean_s[i] != clean_s[len(clean_s)-(i+1)]:
                print(clean_s[i],i)
                return False
        return True