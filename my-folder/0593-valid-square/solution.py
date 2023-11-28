class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dis(x1, x2):
            dis_x = (x2[0] - x1[0]) ** 2
            dis_y = (x2[1] - x1[1]) ** 2
            return sqrt(dis_x + dis_y)

        m = defaultdict(int)
        l = [dis(p1, p2), dis(p1, p3), dis(p1, p4), dis(p2, p3), dis(p2, p4), dis(p3, p4)]
        for num in l:
            m[num] += 1

        if len(m) != 2:
            return False


        side_length, diagonal_length = sorted(m.keys())
        if m[side_length] == 4 and m[diagonal_length] == 2:
            return True

        return False
        

        
        
        

        
