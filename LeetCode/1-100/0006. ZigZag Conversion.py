class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        # 행 증가
        d_row = -1
        row_num = 0
        res_rows = [[] for _ in range(numRows)]
        ans = ""

        for char in s:
            res_rows[row_num].append(char)
            if row_num == 0 or row_num == numRows - 1:
                d_row = d_row * -1
            row_num += d_row

        for row in res_rows:
            ans += ''.join(row)

        return ans