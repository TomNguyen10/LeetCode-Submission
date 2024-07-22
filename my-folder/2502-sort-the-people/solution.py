class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = dict(zip(heights, names))

        sorted_heights = sorted(heights, reverse = True)

        res = [dic[height] for height in sorted_heights]

        return res
