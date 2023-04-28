adj_list = {'A':['B','C'],
            'B':['A'],
            'C':['A','D'],
            'D':['C']}
DFS_output=[]
visited = {}
for node in adj_list.keys():
    visited[node]=False
s="A"
def DFS_iterative(s,adj_list):
    stack=[]
    stack.append(s)
    while stack:
        current = stack.pop()
        if not visited[current]:
            print(current)
            visited[current]=True
            for i in adj_list[current]:
                stack.append(i)
DFS_iterative(s,adj_list)