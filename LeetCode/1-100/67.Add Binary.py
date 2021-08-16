class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 더한다. -> 더한몫을 2로 나눈다. 나머지는 그 자리수가 되고 몫은 다음자리수로 넘어간다.
        res = ''
        carry = 0
        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            res += str(carry % 2)
            carry //= 2

        return res[::-1]