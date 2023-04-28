INF=9999999
N=5
G=[[INF,2,3,INF,INF],
   [2,INF,15,2,INF],
   [3,15,INF,INF,13],
   [INF,2,INF,INF,9],
   [INF,INF,13,9,INF]]
selected={}
for node in range(N):
    selected[node]=False
num_edges=0
selected[0]=True
print("Edges : weight")
while(num_edges < N-1):
    minimum=INF
    a=0
    b=0
    for m in range(N):
        if selected[m]:
            for n in range(N):
                if ((not selected[n]) and G[m][n]!=INF):
                    if minimum>G[m][n]:
                        minimum=G[m][n]
                        a=m
                        b=n
    print(str(a)+"-"+str(b)+":"+str(G[a][b]))
    selected[b]=True
    num_edges += 1
