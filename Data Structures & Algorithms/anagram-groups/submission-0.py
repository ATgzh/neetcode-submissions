class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            sorted_words = "".join(sorted(word))
            groups[sorted_words].append(word)

        return list(groups.values())