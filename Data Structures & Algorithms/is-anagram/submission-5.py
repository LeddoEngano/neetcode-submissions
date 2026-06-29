class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}

        for c in s:
            if c not in hm:
                hm[c] = 1
            else:
                hm[c] += 1

        for c in t:
            if c not in hm:
                return False
            else:
                hm[c] -= 1
        
        values = hm.values()

        for v in values:
            if v > 0:
                return False

        return True