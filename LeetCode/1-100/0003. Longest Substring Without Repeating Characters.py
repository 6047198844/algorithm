class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        table = {}

        # window 를 만들자.
        begin = 0

        for end, char in enumerate(s):
            if char in table and begin <= table[char]:
                begin = table[char] + 1
            table[char] = end
            ans = max(ans, end - begin + 1)

        return ans
