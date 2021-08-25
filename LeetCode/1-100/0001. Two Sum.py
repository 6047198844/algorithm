class Solution(object):
    def twoSum(self, nums, target):
        table = {}
        for i, val in enumerate(nums):
            if val in table:
                return [table[val], i]
                # if a number shows up in the dictionary already that means the necesarry pair has been iterated on previously
            else:  # else is entirely optional
                table[target - val] = i
                # we insert the required number to pair with should it exist later in the list of numbers
