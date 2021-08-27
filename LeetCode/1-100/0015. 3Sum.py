class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        # 2sum으로 변환시킨다.
        # target은 0이다.
        for idx, num in enumerate(nums):
            # 우리는 nums[idx]를 무조건 더할것이다. 따라서 나머지 더한 값들이 nums[idx]를 상쇄시켜줘야한다.
            if idx == 0 or (idx > 0 and nums[idx - 1] != nums[idx]):
                target = -nums[idx]
                table = {}

                for i in nums[idx + 1:]:
                    if i in table:
                        res.append((-target, table[i], i))
                    else:
                        table[target - i] = i

        return set(res)