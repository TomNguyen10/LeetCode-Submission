class Solution {
    public int[] constructRectangle(int area) {
        int[] result = new int[2];
        int a = (int)Math.sqrt(area);
        while(area%a != 0){
            a--;
        }
        int b = area/a;
        result[0] = b;
        result[1] = a;
        return result;
    }
}
