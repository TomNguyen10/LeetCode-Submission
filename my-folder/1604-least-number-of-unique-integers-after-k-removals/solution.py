class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        ct = Counter(arr)
        unique = len(ct)
        sorted_items = sorted(ct.items(), key=lambda x: x[1], reverse=True)
        print(sorted_items)
        for item, count in reversed(sorted_items):
            if k < 0:
                break
            elif k >= count:
                k -= count
                unique -= 1
        return unique
