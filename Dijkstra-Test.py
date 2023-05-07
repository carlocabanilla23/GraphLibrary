import matrixgraph as g

file = open('Dijkstra-Test.txt','r')
line = file.readlines()

elements = line[0].split(' ')

elements[len(elements)-1] = elements[len(elements)-1].strip()



x = g.MatrixGraph(elements)

for i in range(1,len(line)):
    nodes = line[i].split(' ')
    nodes[len(nodes)-1] = nodes[len(nodes)-1].strip()
    p1 = nodes[0]
    p2 = nodes[1]
    w =  nodes[2]
    x.AddWeigthedVertex(p1,p2,w)

print()
print()

print("GRAPH")
x.Print()
print()
print()
d = x.Dijkstra("s","t")
print(d)