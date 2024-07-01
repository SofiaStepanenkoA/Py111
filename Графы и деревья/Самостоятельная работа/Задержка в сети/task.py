from collections import defaultdict
import heapq

def network_delay_time(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    pq = [(0, k)]
    dist = {node: float('inf') for node in range(1, n + 1)}
    dist[k] = 0
    while pq:
        current_time, node = heapq.heappop(pq)

        if current_time > dist[node]:
            continue
        for neighbor, time in graph[node]:
            new_time = current_time + time
            if new_time < dist[neighbor]:
                dist[neighbor] = new_time
                heapq.heappush(pq, (new_time, neighbor))
    max_delay = max(dist.values())
    return max_delay if max_delay != float('inf') else -1