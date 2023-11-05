class Solution:
    def checkString(self, s: str) -> bool:
        bidx = s.find('b')  
        if bidx == -1:
            return True  

        aidx = s.find('a', bidx) 
        return aidx == -1  

