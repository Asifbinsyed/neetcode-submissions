class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for string in strs: 
            sorted_str = "".join(sorted(string))
            seen.setdefault(sorted_str,[]).append(string)

        return list(seen.values())

        