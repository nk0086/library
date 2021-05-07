import heapq
inf = 1 << 64 - 1

def dijkstra(n, G, start):
    #G[i] = (j, cost) cost: i->j の重み
    distance = [inf] * n ; distance[start] = 0
    pre_shortest_path = [-1] * n
    que = [(0, start)]
    heapq.heapify(que) 

    while que:
        cost, v = heapq.heappop(que)
        if distance[v] < cost: continue

        for next_v, cost_v  in G[v]: 
            if distance[next_v] <= distance[v] + cost_v:
                continue

            distance[next_v] = distance[v] + cost_v
            pre_shortest_path[next_v] = v
            heapq.heappush(que, (distance[next_v], next_v))
    
    return distance, pre_shortest_path

def get_shortest_path(pre_shortest_path, t):
    node = t
    res = []
    while node >= 0:
        res.append(node)
        node = path[node]

    return res[::-1]
