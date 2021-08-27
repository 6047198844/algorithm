class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = min(strs, key=len)

        for idx, char in enumerate(ans):
            for str in strs:
                if ans[idx] != str[idx]:
                    return ans[:idx]

        return ans