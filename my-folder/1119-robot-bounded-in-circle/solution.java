class Solution {
    public boolean isRobotBounded(String instructions) {
        int x = 0;
        int y = 0;
        char dir = 'N';

        for (char c : instructions.toCharArray()) {
            if (c == 'G') {
                if (dir == 'N') y++;
                if (dir == 'S') y--;
                if (dir == 'E') x++;
                if (dir == 'W') x--;
            } else if (c == 'L') {
                if (dir == 'N') dir = 'W';
                else if (dir == 'S') dir = 'E';
                else if (dir == 'E') dir = 'N';
                else if (dir == 'W') dir = 'S';
            } else if (c == 'R') {
                if (dir == 'N') dir = 'E';
                else if (dir == 'S') dir = 'W';
                else if (dir == 'E') dir = 'S';
                else if (dir == 'W') dir = 'N';
            }
        }

        if (x == 0 && y == 0) return true;
        return dir != 'N';    
    }
}
