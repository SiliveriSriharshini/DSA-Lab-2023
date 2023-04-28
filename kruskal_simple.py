def kruskal_algo(graph):
    n=len(graph)
    parent = [i for i in range(n)]
    edges=((graph[i][j],i,j)for i in range(n) for j in range(i+1,n) if graph[i][j]!=INF)
    mst=[]
    min_cost=0
    num_edges=0
    while num_edges<n-1:
        for w,u,v in edges:
            if parent[u]!=parent[v]:
                mst.append((u,v,w))
                parent[u]=parent[v]
                min_cost+=w
        num_edges+=1
        print(str(u) + "-" + str(v) + " " + str(w))
    print("mst cost:",min_cost)

INF=9999
graph = [[INF, 2, INF, 6, INF],
         [2, INF, 3, 8, 5],
         [INF, 3, INF, INF, 7],
         [6, 8, INF, INF, 9],
         [0, 5, 7, 9, INF]]
kruskal_algo(graph)