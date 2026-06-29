class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = defaultdict(int)

        for c in s:
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