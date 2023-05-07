
class MatrixGraph:
    graph = []
    size = 0
    node = []

    def __init__(self,elements):
        self.size = len(elements)
        self.node = elements
        for i in range (self.size + 1):
            row = []
            for j in range(self.size + 1):
                row.append(0)
            self.graph.append(row)

        for k in range(0, self.size):
            self.graph[k+1][0] = self.node[k]
            self.graph[0][k+1] = self.node[k]

    def AddVertex(self,n):
        row = []
        self.node.append(n)
        self.size = self.size + 1
        row.append(n)
        for i in range(1,self.size):
            row.append(0)
        # print(row)
        self.graph.append(row)
      
        rheader = self.graph[0]
        rheader.append(n)
        self.graph[0] = rheader
        for k in range(1,self.size+1):
            tmp = self.graph[k]
            tmp.append(0)
            self.graph[k] = tmp

    def Print(self):
        for i in range (0,self.size+1):
            for j in range(0,self.size+1):
                print("| " +str(self.graph[i][j]) + " " , end='')
            print("|")

    def AddEdge(self,a,b):
        p1 = self.node.index(a) + 1
        p2 = self.node.index(b) + 1
        self.graph[p1][p2] = 1

    def AddBiconnectedEdge(self,a,b):
        p1 = self.node.index(a) + 1
        p2 = self.node.index(b) + 1
        self.graph[p1][p2] = 1
        self.graph[p2][p1] = 1

    def BFS(self,n):
        print(n)
        queue = []
        L = []
        isVisited = ["F"] * self.size

        queue.append(n)

        pos = self.node.index(n)

        isVisited[pos] = "T"

        while (len(queue) > 0):
            v = queue.pop()
            x = self.node.index(v) + 1

            l =  len(self.node) + 1

            for i in range(l):
                if (self.graph[x][i] == 1):
                    if (isVisited[i-1] == "F"):
                        L.append([v,self.node[i-1]])
                        print(self.node[i-1])
                        queue.append(self.node[i-1])
                        isVisited[i-1] = "T"

        return L

    def DFS(self,n):
        print(n)
        queue = []
        L = []
        isVisited = ["F"] * self.size

        queue.append(n)

        pos = self.node.index(n)

        isVisited[pos] = "T"

        while (len(queue) > 0):
            v = queue.pop(0)
            x = self.node.index(v) + 1

            l =  len(self.node) + 1

            for i in range(l):
                if (self.graph[x][i] == 1):
                    if (isVisited[i-1] == "F"):
                        L.append([v,self.node[i-1]])
                        print(self.node[i-1])
                        queue.append(self.node[i-1])
                        isVisited[i-1] = "T"

        return L

    def RemoveEdge(self,a,b):
        p1 = self.node.index(a) + 1
        p2 = self.node.index(b) + 1
        self.graph[p1][p2] = 0
 
    def AddWeigthedVertex(self,a,b,w):
        p1 = self.node.index(a) + 1
        p2 = self.node.index(b) + 1
        self.graph[p1][p2] = w

    def FindWeight(self,a,b):
        p1 = self.node.index(a) + 1
        p2 = self.node.index(b) + 1
        # print(self.graph[p1][p2])
        return self.graph[p1][p2]

    def FindVertex(self,n):
        Vertex = []
        x = self.node.index(n) + 1
        row = self.graph[x]

        for i in range(1,len(row)):
            if (row[i] != 0):
                Vertex.append(self.node[i-1])
        return Vertex
    
    def IsAllNodesVisited(self,arr):
        for n in arr:
            if (n == True):
                return False
        return True

    def FindPath(self,a,b):
        isVisited = self.CreateBoolTable(False)
        # Create a stack
        stack = []
        # Push a into the stack
        stack.append(a)
        # mark a as visited
        while (len(stack) >= 0):
            head = stack[0]
            if (head == b):
                result = []
                for s in stack:
                    sidx = self.node.index(s)   
                    if (isVisited[sidx] == True):
                        result.append(s)
                result.insert(0,b)
                result.reverse()
                return result
            idx = self.node.index(head)
            isVisited[idx] = True
        # look for all the neighbors of a that is not visited
            neighbor = self.FindVertex(head)
            tmpNeighbor = []
            for n in neighbor:
                nidx = self.node.index(n)
                if (isVisited[nidx] == False):
                    tmpNeighbor.append(n)
            neighbor = tmpNeighbor
            # print(len(neighbor))
        # If there is a has no neighbor pop until we reach the head of the stack that is still not visible
            if (len(neighbor) == 0):
                while(isVisited[self.node.index(stack[0])] == True):
                    stack.pop(0)
        # Else push all the neighbors of a into the stack
            else:
                for v in neighbor:
                    stack.insert(0,v)

        return stack

# Check if Graph is Bipartite

    # Create a 2d matrix for marking of color
    def Create2dMatrix(self,size):
        graph = []
        for i in range (size + 1):
            row = []
            for j in range(size + 1):
                row.append(0)
            graph.append(row)

        return graph
    
    def CreateBoolTable(self,size):
        boolTable = []

        for i in range(0,size-1):
            boolTable.append(False)
        
        return boolTable
    
    def IsBipartite(self):
        coloredGraph = self.Create2dMatrix(len(self.node))
        isVisited = self.CreateBoolTable(len(self.node)+1)

        n = self.node[0]

        coloredGraph[0][0] = -1
        queue = []
        L = []
        
        queue.append(n)

        while (len(queue) > 0):
            v = queue.pop()
            x = self.node.index(v)
            isVisited[x] = True

            headColor = coloredGraph[x][x]

            neighbor = self.FindVertex(v)

            for n in neighbor:
                npos = self.node.index(n)
                color = coloredGraph[npos][npos]

                if (color == headColor):
                    # print(coloredGraph)
                    return False
                if (color == 0):
                    if (headColor == 1):
                        coloredGraph[npos][npos] = -1
                        queue.append(n)
                    else:
                        coloredGraph[npos][npos] = 1
                        queue.append(n)

        # print(coloredGraph)
        return True
    
# Dijkstra 
    def Dijkstra(self,s,t):
        Neighbor = self.FindVertex(s)
        S = []
        D = [-1]*self.size
        D[self.node.index(s)] = 0
        for n in Neighbor:
            v = self.node.index(n)
            D[v] = int(self.FindWeight(s,n))
        S.append(s)

        # print(S)
        while ((len(self.node) - len(S)) != 0):
            VS = []
            for n in self.node:
                if n not in S:
                    VS.append(n)

            curr = -1
            npos = -1
            # print(VS)
            for vs in VS:
                i = self.node.index(vs)
        
                if (curr == -1):
                    if (D[i] == -1):
                        # print("1")
                        curr = curr
                        npos = npos
                    else:
                        # print("2")
                        curr = D[i]
                        npos = i
                else:
                    if (D[i] == -1):
                        # print("3")
                        curr = curr
                        npos = npos
                    elif (D[i] < curr):
                        # print("4")
                        curr = D[i]
                        npos = i
                        # print(i)
                # print(D)
            u = self.node[npos]
            
            S.append(u)
            # print(S)
            UV = self.FindVertex(u)
            for v in UV:
                vi = self.node.index(v)
                ui = self.node.index(u)
                if ( (D[vi] > D[ui] + int(self.FindWeight(u,v))) or (D[vi] == -1) ):
                    D[vi] = D[ui] + int(self.FindWeight(u,v))
        D.sort()
        D.reverse()
        print("Shortest Path " + str(D[0]))
        return S