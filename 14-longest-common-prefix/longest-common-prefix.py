class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        prefix_len = len(prefix)

        for i in strs[1:]:
            while i[:prefix_len] != prefix:
                prefix_len-=1
                prefix = prefix[:prefix_len]
        
        return prefix