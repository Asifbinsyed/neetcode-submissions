class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            length = [len(x) for x in strs]
            if len(strs) == 0:
                return ""

            if len(strs) == 1:
                return strs[0]

            min_len = min(length)

            reference = strs[0]
            for i in range(min_len):
                for word in strs[1:]:
                    if reference[i] != word[i]:
                        return reference[:i]
            return reference[:min_len]

        