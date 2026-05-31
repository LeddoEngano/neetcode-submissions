class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        
        # iterate in revers
        # check rightMax
        # arr[i] = rightMax

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        
        return arr
