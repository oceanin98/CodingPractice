import sys


def find(pr, v, inter):
    if pr[v][0] == v:
        for subp in inter:
            pr[subp][0] = v
            pr[subp][1] = pr[v][1] - 1
        return v

    else:
        inter.append(pr[v][0])
        return find(pr, pr[v][0], inter)


def union(pr, u, v):
    if pr[u][1] > pr[v][1]:
        pr[v][0] = u
    elif pr[u][1] < pr[v][1]:
        pr[u][0] = v
    else:
        pr[u][0] = v
        pr[v][1] += 1


def kruskal(N, K, edges, edgeinfo):
    edges.sort(key=lambda edge: edge[2])
    #edges.sort(key=lambda edge: edgeinfo[edge[0]])
    MST = []

    parents_ranks = []

    for i in range(N):
        parents_ranks.append([i, 0])

    curmin = -K
    for edge in edges:
        u, v, c = edge
        if c - curmin < K:
            continue

        u_inter = []
        v_inter = []
        root_u = find(parents_ranks, u, u_inter)
        root_v = find(parents_ranks, v, v_inter)
        if root_u != root_v:
            MST.append(edge)
            curmin = c
            if len(MST) == N - 1:
                break
            union(parents_ranks, root_u, root_v)

    if len(MST) < N - 1:
        return "NO"
    else:
        wsum = 0
        for e in MST:
            wsum += e[2]
        return wsum


def read_ints():
    temp = input().split()
    temp = [int(t) for t in temp]
    return temp


tests = int(input())

for _ in range(tests):
    N, M, K = read_ints()

    max_c = 0
    min_c = sys.maxsize

    edges = []
    edgeinfo = [0] * N
    for _ in range(M):
        u, v, c = read_ints()

        edgeinfo[u] += 1
        edgeinfo[v] += 1

        if min_c > c:
            min_c = c
        elif max_c < c:
            max_c = c

        edges.append((u, v, c))
        #edges.append((v,u,c))

    # CHeck if there are enough number of edges
    if M < N - 1:
        print("NO")
        continue

    # Check if there are enough edges with K apart
    if (max_c - min_c) / K + 1 < N - 1:
        print("NO")
        continue

    result = kruskal(N, K, edges, edgeinfo)
    print(result)
