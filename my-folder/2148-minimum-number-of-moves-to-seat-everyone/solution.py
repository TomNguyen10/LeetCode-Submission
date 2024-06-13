class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        max_val = max(seats)
        max_val = max(max_val, max(students))

        arr = [0] * (max_val + 1)

        for seat in seats:
            arr[seat] += 1
        
        for student in students:
            arr[student] -= 1
        
        moves = 0
        unmatched = 0
        for difference in arr:
            moves += abs(unmatched)
            unmatched += difference

        return moves
