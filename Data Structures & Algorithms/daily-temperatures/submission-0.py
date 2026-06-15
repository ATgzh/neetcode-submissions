class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        for i in range(len(temperatures)-1):
            right = i+1
            while right < len(temperatures):
                if temperatures[right] > temperatures[i]:
                    res[i] = right - i
                    break
                else:
                    right += 1
        return res