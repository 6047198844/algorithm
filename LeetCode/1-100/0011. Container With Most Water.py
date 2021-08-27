class Solution:
    def maxArea(self, height: List[int]) -> int:
        height = deque(height)
        begin = 0
        end = len(height) - 1
        ans = 0

        while begin < end:
            container = min(height[begin], height[end]) * (end - begin)
            ans = max(ans, container)
            if height[begin] <= height[end]:
                begin += 1
            else:
                end -= 1

        return ans