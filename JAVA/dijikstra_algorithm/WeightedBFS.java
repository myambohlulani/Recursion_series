package dijikstra_algorithm;

import java.util.*;

public class WeightedBFS {
    public int dijikstra(Map<Integer, List<int[]>> graph, int start, int target, int n) {
        int[] dist = new int[n + 1];

        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;

        // min heap: [const, node]
        PriorityQueue<int[]> priorityQue = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        priorityQue.offer(new int[] { 0, start });

        while (!priorityQue.isEmpty()) {
            int[] current = priorityQue.poll();

            int cost = current[0], node = current[1];

            if (node == target) {
                return cost;
            }

            for (int[] neighbour : graph.getOrDefault(node, new ArrayList<>())) {
                int nextNode = neighbour[0], weight = neighbour[1];
                int newDist = cost + weight;

                if (newDist < dist[nextNode]) {
                    dist[nextNode] = newDist;
                    priorityQue.offer(new int[] { newDist, nextNode });
                }
            }

        }

        // unreachable
        return -1;
    }
}
