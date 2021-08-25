class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: 공백제거
        s = s.lstrip()
        if not s:
            return 0

        # Step 2: 부호추출
        sign = ""
        if s[0] == "-" or s[0] == "+":
            sign = s[0]
            s = s[1:]
        res = sign + "0"

        # Step 3: 앞에서부터 숫자를 추출
        for n in s:
            if n.isdigit():
                res += n
            else:
                break

        # Step 4: int로 변환
        res = int(res)

        # Step 5: 범위 확인
        min_value = -2 ** 31
        max_value = 2 ** 31 - 1

        if res < min_value:
            return min_value
        if res > max_value:
            return max_value

        # Step 6: 반환
        return res