class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        hm = {}

        for s in students:
            if s not in hm:
                hm[s] = 1
            else:
                hm[s] += 1
        
        for s in sandwiches:
            if hm.get(s, 0) > 0:
                res -= 1
                hm[s] -= 1 
            else:
                return res
    
        return res