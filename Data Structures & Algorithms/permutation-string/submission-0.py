class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        count2 = {}

        if len(s1) > len(s2):
            return False

        for x in s1:
            if x not in count1:
                count1[x] = 1
            else:
                count1[x] += 1

        for x in range(len(s1)):
            char = s2[x]
            if char not in count2:
                count2[char] = 1
            else:
                count2[char] += 1

        if count1 == count2:
                return True

        for x in range(len(s2)-len(s1)):
            leaving = s2[x]
            count2[leaving] -= 1

            if count2[leaving] == 0:
                del count2[leaving]
            
            entering = s2[x + len(s1)]
            if entering not in count2:
                count2[entering] = 1
            else:
                count2[entering] += 1
            
            if count1 == count2:
                return True
        return False
