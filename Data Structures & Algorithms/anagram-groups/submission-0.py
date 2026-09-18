class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            new_str = sorted(word)
            use_this = "".join(new_str)
            groups[use_this] = groups.get(use_this, []) + [word]
        return list(groups.values())

        
        