class Solution {
    
    int[] number = {8, 4, 2, 1, 32, 16, 8, 4, 2, 1};
    
    public List<String> readBinaryWatch(int turnedOn) {
        ArrayList<String> read = new ArrayList<String>();
        help(0,0,0,turnedOn, read);
        return read;
    }
    
    private void help (int hour, int min, int index, int num, ArrayList<String>read){
        if (hour > 12 || min >= 60 || hour == 12 && min == 0) {
            return;
        }
        if (num == 0) {
            String strMin = String.valueOf(min);
            if (strMin.length() == 1) 
                strMin = "0" + strMin;
            read.add(String.valueOf(hour) + ":" + strMin);
        }
        else if (index < 10 && num <= 10 - index && num > 0) {
            help(hour, min, index+1, num, read);
            if (index < 4) 
                help (hour + number[index], min, index + 1, num - 1, read);
            else 
                help (hour, min + number[index], index + 1, num - 1, read);
        }
    }
}
