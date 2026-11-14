class Solution:
    def isPalindrome(self, s: str) -> bool:
        small = s.lower()
        r = len(s)-1
        l = 0
        while l < r:
            while l < r and not small[l].isalnum():
                l += 1
            while l < r and not small[r].isalnum():
                r -= 1
            if small[r] != small[l]:
                return False
            l += 1
            r -= 1
        return True