class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ones = students.count(1)
        zeros = students.count(0)

        for val in sandwiches:
            if val == 0:
                if zeros == 0: return ones
                zeros -= 1
            else:
                if ones == 0: return zeros
                ones -= 1
        
        return 0
