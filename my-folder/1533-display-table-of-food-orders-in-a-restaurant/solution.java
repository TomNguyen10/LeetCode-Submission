public class Solution {
    public List<List<String>> displayTable(List<List<String>> orders) {
        // HashMap to store the count of each food item ordered by each table
        Map<Integer, Map<String, Integer>> foodCount = new HashMap<>();
        // TreeSet to store all the unique food items in alphabetical order
        TreeSet<String> foodItems = new TreeSet<>();

        // Iterate through the orders and update foodCount and foodItems
        for (List<String> order : orders) {
            String customerName = order.get(0);
            int tableNumber = Integer.parseInt(order.get(1));
            String foodItem = order.get(2);

            // Update foodCount
            Map<String, Integer> tableCount = foodCount.getOrDefault(tableNumber, new HashMap<>());
            tableCount.put(foodItem, tableCount.getOrDefault(foodItem, 0) + 1);
            foodCount.put(tableNumber, tableCount);

            // Update foodItems
            foodItems.add(foodItem);
        }

        // Create the result ArrayList
        List<List<String>> result = new ArrayList<>();

        // Create the header row
        List<String> headerRow = new ArrayList<>();
        headerRow.add("Table");
        headerRow.addAll(foodItems);
        result.add(headerRow);

        // Sort the table numbers in ascending order
        List<Integer> sortedTables = new ArrayList<>(foodCount.keySet());
        sortedTables.sort(null);

        // Iterate through the sorted table numbers
        for (int tableNumber : sortedTables) {
            Map<String, Integer> tableCount = foodCount.get(tableNumber);
            List<String> tableRow = new ArrayList<>();
            tableRow.add(String.valueOf(tableNumber));

            // Populate the table row with the food item counts
            for (String foodItem : foodItems) {
                int count = tableCount.getOrDefault(foodItem, 0);
                tableRow.add(String.valueOf(count));
            }

            result.add(tableRow);
        }

        return result;
    }
}

