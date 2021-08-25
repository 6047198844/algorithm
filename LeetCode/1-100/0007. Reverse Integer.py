class Solution:
    def reverse(self, x: int) -> int:
        sign = [+1,-1][x<0]
        x = sign * int(str(abs(x))[::-1])
        if -(2**31) <= x <= 2**31:
            return x
        return 0