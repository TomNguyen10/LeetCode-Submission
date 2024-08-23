class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            new = [1]
            for j in range(1, len(row)):
                new.append(row[j-1] + row[j])
            new.append(1)
            row = new
        return row
