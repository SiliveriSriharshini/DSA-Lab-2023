
def find(i):
	while parent[i] != i:
		i = parent[i]
	return i


def union(i, j):
	a = find(i)
	b = find(j)
	parent[a] = b

def kruskalMST(cost):
	for i in range(V):
		parent[i] = i
	edge_count = 0
	mincost=0
	while edge_count < V - 1:
		min = INF
		a = -1
		b = -1
		for i in range(V):
			for j in range(V):
				if (find(i) != find(j) and cost[i][j] < min):
					min=cost[i][j]
					a = i
					b = j
		union(a, b)
		print('Edge {}:({}, {}) cost:{}'.format(edge_count, a, b, min))
		edge_count += 1
		mincost += min
	print("Minimum cost= {}".format(mincost))
V=5
parent = [i for i in range(V)]
INF = float('inf')
cost = [[INF, 2, INF, 6, INF],
		[2, INF, 3, 8, 5],
		[INF, 3, INF, INF, 7],
		[6, 8, INF, INF, 9],
		[INF, 5, 7, 9, INF]]
kruskalMST(cost)



