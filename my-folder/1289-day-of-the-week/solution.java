class Solution {
    public String dayOfTheWeek(int day, int month, int year) {
        String[] days = new String[]{"Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"};
        if (month < 3) {
            month += 12;
            year--;
        }
        int res = (day + (13*(month + 1)/5) + year%100 + (year%100)/4 + (year/100)/4 + 5*(year/100)) % 7;
        return days[res];
    }
}
