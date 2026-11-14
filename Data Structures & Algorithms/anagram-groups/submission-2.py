class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for words in strs:
            word = tuple(sorted(words))
            if word not in group:
                group[word] = []
            group[word].append(words)
        return list(group.values())
