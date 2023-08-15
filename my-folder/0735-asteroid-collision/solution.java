class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();
        for (int i : asteroids) {
            if (i > 0) {
                stack.push(i);
            }
            while (!stack.isEmpty() && stack.peek() > 0 && stack.peek() < Math.abs(i)) {
                stack.pop();
            }
            if (stack.isEmpty() || stack.peek() < 0) {
                stack.push(i);
            }
            else if (i + stack.peek() == 0) {
                stack.pop();
            }
        }
        int[] res = new int[stack.size()];
        for (int i = res.length - 1; i >= 0; i--) {
            res[i] = stack.pop();
        }
        return res;
    }
}
