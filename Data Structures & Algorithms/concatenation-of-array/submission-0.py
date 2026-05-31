class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2 * len(nums))

        for i in range(2):
            for n in range(len(nums)):
                if (i == 1):
                    ans[n] = nums[n]
                else:
                    ans[n + len(nums)] = nums[n]

        return ans