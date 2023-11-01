class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left, right, count = 0, 0, 0
        ans = float('inf')
        while right < len(blocks):
            if blocks[right] == 'W':
                count += 1
            if right - left + 1 == k:
                ans = min(ans, count)
                if blocks[left] == 'W':
                    count -= 1
                left += 1
            right += 1
        return ans
            

        
