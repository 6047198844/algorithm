'''
dividend를 divisor로 나누는 문제
단, 곱셈/나눗셈/mod 연산은 제외한다.

남은 연산은 더하기 / 빼기 밖에 없다.
빼기를 사용해보자.
dividend가 divisor보다 작을때까지 빼면 될것같다. -> brute force
하지만, 이 방법 사용시 dividend가 2^31 - 1 , divisor가 1일 경우 2^31 - 1번의 뺄셈이 이루어져야 한다.
따라서 divisor가 뺄셈 성공시에 2배로 늘려서 위의 과정을 반복한다.
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        if dividend < divisor:
            return 0

        res = 0
        cnt = 1
        ndivisor = divisor
        while dividend >= ndivisor:
            dividend -= ndivisor
            res += cnt
            # 2배
            cnt <<= 1
            ndivisor <<= 1

        res += self.divide(dividend, divisor)

        if positive == False:
            res = -res

        if -2 ** 31 <= res <= 2 ** 31 - 1:
            return res
        return 2 ** 31 - 1