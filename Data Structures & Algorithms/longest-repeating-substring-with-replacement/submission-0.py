class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_count = 0
        max_len = 0

        for right in range(len(s)):
            char = s[right]
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
            max_count = max(max_count, count[char])
            while(right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            max_len = max(right-left+1, max_len)
        
        return max_len