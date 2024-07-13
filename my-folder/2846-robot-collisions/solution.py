from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = list(zip(positions, healths, directions, range(len(positions))))
        robots.sort(key=lambda x: x[0])
        
        stack = [] 
        for pos, health, direction, index in robots:
            if direction == 'R':
                stack.append((pos, health, direction, index))
            else:
                while stack and stack[-1][2] == 'R':
                    r_pos, r_health, r_direction, r_index = stack.pop()
                    if health > r_health:
                        health -= 1
                    elif health < r_health:
                        stack.append((r_pos, r_health - 1, r_direction, r_index))
                        health = 0
                        break
                    else:
                        health = 0
                        break
                
                if health > 0:
                    stack.append((pos, health, direction, index))
        
        survivors = sorted(stack, key=lambda x: x[3])
        result = [health for pos, health, direction, index in survivors]
        
        return result

