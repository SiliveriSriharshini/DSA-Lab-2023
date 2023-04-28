from queue import Queue
adj_list = {'A':['B','C'],
            'B':['A'],
            'C':['A','D'],
            'D':['C']}
BFS_output=[]
visited = {}
queue = Queue()
for node in adj_list.keys():
    visited[node]=False
s = 'A'
visited[s]=True
queue.put(s)
while not queue.empty():
    u=queue.get()
    BFS_output.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v]=True
            queue.put(v)
print(BFS_output)