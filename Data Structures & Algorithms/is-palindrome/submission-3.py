class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = len(s)-1
        left = 0
        slower = s.lower()
        while left < right:
            while left < right and not slower[left].isalnum():
                left += 1
            while left < right and not slower[right].isalnum():
                right -= 1

            if slower[left] != slower[right]:
                return False

            left += 1
            right -= 1
            
        return True