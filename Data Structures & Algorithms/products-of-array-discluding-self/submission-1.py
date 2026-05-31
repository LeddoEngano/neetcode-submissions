class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hmCount = {}

        pos = 0
        for i, v in enumerate(nums):
            pos = i
            value = 1
            for idx, va in enumerate(nums):
                if idx == pos:
                    continue
                else:
                    value = va * value
            hmCount[i] = value

        return list(hmCount.values())