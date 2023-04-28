from queue import Queue
def add_node(v):
    nodes=[]
    graph=[]
    node_count=0
    if v in nodes:
        print("v is already present")
    else:
        nodes.append(v)
        node_count+=1
        for n in graph:
            n.append(v)
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)
def add_edge(u,v,w):
    global nodes, graph
    if v not in nodes:
        print("v not in nodes")
    if u not in nodes:
        print("u not in nodes")
    else:
        index1=nodes.index(u)
        index2=nodes.index(v)
        graph[index1][index2]=w
def delete_node(v):
    global node_count,nodes,graph
    if v not in nodes:
        print("v is not present")
    else:
        index1=nodes.index(v)
        node_count-=1
        nodes.remove(v)
        graph.pop(index1)
        for i in range(graph):
            i.pop(index1)
def delete_edge(v1,v2):
    if v1 or v2 not in nodes:
        print("nodes not present")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=0
        graph[index2][index1]=0
adj_list = {'A':['B','C'],
            'B':['A'],
            'C':['A','D'],
            'D':['C']}
visited={}
visited_bfs={}
bfs_output=[]
q=Queue()
s="A"
visited_bfs[s]=True
q.put(s)
for i in adj_list:
    visited[i]=False
def dfs_graph(visited,adj_list,n):
    if not visited[n]:
        print(n)
        visited[n]=True
        for i in adj_list(n):
            dfs_graph(adj_list,i)
for i in adj_list:
    visited_bfs[i]=False
while not q.empty():
    u=q.get()
    bfs_output.append(u)
    for v in adj_list(u):
        if not visited_bfs[v]:
            visited_bfs[v]=True
            q.put(v)
print(bfs_output)
dfs_graph(visited,adj_list,s)
#prims algo
INF=9999999
n=5
G=[[INF,2,3,INF,INF],
   [2,INF,15,2,INF],
   [3,15,INF,INF,13],
   [INF,2,INF,INF,9],
   [INF,INF,13,9,INF]]
selected={}
for i in range(n):
    selected[i]=False
selected[0]=True
num_edges=0
print("edges"+":"+"cost")
while num_edges<n:
    min=INF
    a=0
    b=0
    for m in range(n):
        if selected[m]:
            for i in range(n):
                if not selected[i] and G[m][i]!=INF:
                    if G[m][i]<min:
                        min=G[m][i]
                        a=m
                        b=i
    print(str(a)+"-"+str(b)+" "+str(min))
    selected[b]=True
    num_edges+=1
#kruskal
'''selectedk={}
for i in range(n):
    selectedk[i]=False'''
mst=[]
min_cost=0
parent=list(range(n))
edge=sorted((G[i][j],i,j)for i in range(n) for j in range(i+1,n) if G[i][j] != INF)
for w,u,v in edge:
    '''if selected[v]:
        print("already selected")'''
    if parent[u]!=parent[v]:
        mst.append((u,v,w))
        parent[u]=parent[v]
        #selected['v']=True
        min_cost+=w
        print(str(u) + "-" + str(v) + " " + str(w))
print("mst cost:", min_cost)




