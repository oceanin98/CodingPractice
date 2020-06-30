from collections import deque

def read_ints():
    temp = input().split()
    ints = [int(t) for t in temp]
    return ints

def get_MST(G, S):
    
    #Compulsory?
    # Wasn't compulsory LOL
    return 0

def lowerbound(graph, S, u, v, cost):
    min_from_u = 10001
    for neighbour in graph[u]:
        if neighbour not in S:
            min_from_u = min(min_from_u, graph[u][neighbour])
    if min_from_u == 10001:
        return 70*10000

    min_from_v = 10001
    for neighbour in graph[v]:
        if neighbour not in S:
            min_from_v = min(min_from_v, graph[v][neighbour])
    if min_from_v == 10001:
        return 70*10000

    MST = get_MST(graph, S) 
    if MST < 0:
        return 70 * 10000

    return MST + min_from_u + min_from_v + cost

def TSP(graph, n):
    minpath = 10000 * 70
    queue = deque()
    queue.append([0,[0],0,0])

    while queue:
        subproblem = queue.popleft()
        u, S, v, cost = subproblem
        for neighbour in graph[v]:
            if neighbour not in S: # x in V-S
                S_ = S[:]
                cost_ = cost + graph[v][neighbour]
                S_.append(neighbour)
                if len(S_) == n:
                    if neighbour in graph[u]:
                        minpath = min(minpath, cost_ + graph[u][neighbour])
                else:
                    if lowerbound(graph, S_, u, neighbour, cost_) < minpath:
                        queue.append([u,S_,neighbour,cost_])
    if minpath == 10000 * 70:
        return -1
    return minpath

test = int(input())

for _ in range(test):
    n,m = read_ints()

    graph = {}
    for _ in range(m):
        u,v,c = read_ints()
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v] = c
        graph[v][u] = c
    
    result = TSP(graph, n)
    print(result)
