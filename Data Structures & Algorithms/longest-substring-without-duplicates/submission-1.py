class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        long = 0
        l, r = 0, 0
        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            long = max(long, r-l+1)
            r += 1
        return long



