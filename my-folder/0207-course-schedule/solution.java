import java.util.ArrayList;
import java.util.List;

public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] prerequisite : prerequisites) {
            int course = prerequisite[0];
            int prerequisiteCourse = prerequisite[1];
            graph.get(course).add(prerequisiteCourse);
        }

        boolean[] visited = new boolean[numCourses];
        boolean[] dfsVisited = new boolean[numCourses];

        for (int i = 0; i < numCourses; i++) {
            if (!visited[i] && hasCycle(graph, visited, dfsVisited, i)) {
                return false;
            }
        }

        return true;
    }

    private boolean hasCycle(List<List<Integer>> graph, boolean[] visited, boolean[] dfsVisited, int course) {
        visited[course] = true;
        dfsVisited[course] = true;

        for (int prerequisiteCourse : graph.get(course)) {
            if (!visited[prerequisiteCourse]) {
                if (hasCycle(graph, visited, dfsVisited, prerequisiteCourse)) {
                    return true;
                }
            } else if (dfsVisited[prerequisiteCourse]) {
                return true;
            }
        }

        dfsVisited[course] = false;
        return false;
    }
}

