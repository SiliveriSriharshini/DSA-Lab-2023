adj_list = {'A':['B','C'],
            'B':['A'],
            'C':['A','D'],
            'D':['C']}
DFS_output=[]
visited = {}
for node in adj_list.keys():
    visited[node]=False
s="A"
def dfs(visited,adj_list,n):
    if not visited[n]:
        print(n)
        visited[n]=True
        for node in adj_list[n]:
            dfs(visited, adj_list,node)

dfs(visited,adj_list,s)
