class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win_count = defaultdict(int)
        lose_count = defaultdict(int)

        for match in matches:
            winner, loser = match[0], match[1]
            win_count[winner] += 1
            lose_count[loser] += 1

        not_lost_any = [player for player in win_count.keys() if lose_count[player] == 0]

        lost_once = [player for player in lose_count.keys() if lose_count[player] == 1]

        not_lost_any.sort()
        lost_once.sort()

        return [not_lost_any, lost_once]
