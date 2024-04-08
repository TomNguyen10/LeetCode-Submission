class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m1 = defaultdict(int)
        m2 = defaultdict(int)
        for char in s1:
            m1[char] += 1
        for char in s2[:len(s1)]:
            m2[char] += 1

        if m1 == m2: return True

        for right in range(len(s1), len(s2)):
            left = right - len(s1)
            m2[s2[left]] -= 1
            if  m2[s2[left]] == 0:
                del m2[s2[left]]
            m2[s2[right]] += 1

            if m1 == m2: return True
        
        return False
