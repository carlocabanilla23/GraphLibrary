import listgraph as g

file = open('test.txt','r')
line = file.readlines()

elements = line[0].split(' ')

elements[len(elements)-1] = elements[len(elements)-1].strip()

x = g.ListGraph(elements)

for i in range(1,len(line)):
    nodes = line[i].split(' ')
    nodes[len(nodes)-1] = nodes[len(nodes)-1].strip()
    p1 = nodes[0]
    p2 = nodes[1]
    x.AddBiconnectedEdge(p1,p2)

x.AddVertex("X")
print("Adjacency List")
x.Print()
print()
print("BFS")
bfsResult = x.BFS("A")
print(bfsResult)
print("DFS")
dfsResult = x.BFS("A")
print(dfsResult)
print("Edge")
edges = x.FindVertex("A")
print(edges)
print("Path")
path = x.FindPath("B","F")
print(path)
print("Dikjstra", end='')
dikstra = x.Dijkstra("B","F")
print(" Shortest Path : " + str(dikstra))

arr = [1,2,3]
