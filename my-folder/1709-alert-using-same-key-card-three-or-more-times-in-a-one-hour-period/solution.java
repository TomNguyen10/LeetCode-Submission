import java.util.*;

class Solution {
    public List<String> alertNames(String[] keyName, String[] keyTime) {
        Map<String, List<Integer>> map = new HashMap<>();

        for (int i = 0; i < keyName.length; i++) {
            String name = keyName[i];
            int time = convertToMinutes(keyTime[i]);

            if (!map.containsKey(name)) {
                map.put(name, new ArrayList<>());
            }

            List<Integer> times = map.get(name);
            times.add(time);
        }

        List<String> res = new ArrayList<>();
        for (Map.Entry<String, List<Integer>> entry : map.entrySet()) {
            String name = entry.getKey();
            List<Integer> times = entry.getValue();
            if (hasAlert(times)) {
                res.add(name);
            }
        }

        Collections.sort(res);
        return res;
    }

    private int convertToMinutes(String time) {
        int hour = Integer.parseInt(time.substring(0, 2));
        int minute = Integer.parseInt(time.substring(3));
        return hour * 60 + minute;
    }

    private boolean hasAlert(List<Integer> times) {
        Collections.sort(times);

        for (int i = 2; i < times.size(); i++) {
            int diff = times.get(i) - times.get(i - 2);
            if (diff <= 60) {
                return true;
            }
        }

        return false;
    }
}

