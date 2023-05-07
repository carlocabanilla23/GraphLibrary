# Graph Library
## Description
Graph Library implemented using a python. There two different kind of implementation that can be use to create a graph and separated with their own class. <br/>

### How to use
 
 Adjacency Matrix Graph
```python
  import matrixgraph as g
  graph = g.MatrixGraph(elements) // elements is a list of nodes
```

Adjacency List Graph
```python
  import listgraph as g
  graph = g.ListGraph(elements) // elements is a list of nodes
```

  

## Adjacency Matrix

### Class Attributes
| Attribute | Description   |
| :---         |     :---      |
| graph        | 2D Jagged array that stores the value of each nodes and vertices  |
| size         | Int that stores the size of the elements in the graph     |
| node         | Array that stores all the vertices in the graph           |

### Class Method
| Method | Description |
| :---         |     :---      |
| AddVertex | Add Vertex to the graph|
| AddEdge | Add Edge to the Graph with a defualt weigh of 1 |
| Print | Print the Graph|
| AddBiconnectedEdge | Add a two way edge with a default weight of 1 |
| BFS | Performs a Breadth-First Search traversal to the graph |
| DFS | Performs a Depth-First Search traversal to the graph |
| RemoveEdge | Remove Edge to the graph|
| AddWeightedVertex | Add a one way edge between two nodes that has a weight |
| FindWeight | Find the weight of the edge between two nodes |
| FindVertex | Find all the neightbor of a node |
| IsAllNodeVisited | Take an array of bool and check if all the element is true or false |
| FindPath | Find the the path from one node to another node |
| Create2dMatrix | Create a 2Dmatrix based on number of nodes. The matrix will start without any edge |
| CreateBoolTable | Create an array that will take a bool element. All the element are initially set to false |
| IsBipartite | Check if the graph is bipartite graph |
| Dijkstra | Performs a Dijkstra algorithm to print the shortest path and return the path using an array |



## Adjacency List

### Class Attributes
| Attribute | Description   |
| :---         |     :---      |
| graph        | 2D array that stores the value of each nodes and vertices |
| size         | Int that stores the size of the elements in the graph     |
| node         | Array that stores all the vertices in the graph           |

### Class Method
| Method | Description |
| :---         |     :---      |
| AddVertex | Add Vertex to the graph|
| AddEdge | Add Edge to the Graph with a defualt weigh of 1 |x
| Print | Print the Graph|
| AddBiconnectedEdge | Add a two way edge with a default weight of 1 |
| BFS | Performs a Breadth-First Search traversal to the graph |
| DFS | Performs a Depth-First Search traversal to the graph |
| RemoveEdge | Remove Edge to the graph|
| AddWeightedEdge | Add a one way edge between two nodes that has a weight |
| FindWeight | Find the weight of the edge between two nodes |
| FindVertex | Find all the neightbor of a node |
| IsAllNodeVisited | Take an array of bool and check if all the element is true or false |
| FindPath | Find the the path from one node to another node |
| CreateBoolTable | Create an array that will take a bool element. All the element are initially set to false |
| Dijkstra | Performs a Dijkstra algorithm to print the shortest path and return the path using an array |


### Test
Adjacency Matrix Graph
```bash
  python.exe .\main.py
```
Adjacency List Graph
```bash
  python.exe .\list-graph-test.py
```

Test Graph Bipartiness
```bash
  python.exe .\TestBipartite.py  
```

Test Dijstra Algorithm and FInd the shortest Path
```bash
  python.exe .\Dijkstra-Test.py
```
