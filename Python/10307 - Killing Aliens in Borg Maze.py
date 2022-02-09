import sys
import heapq

#directions the army can travel in the maze (y,x)
directions = {"left": (0,-1), "right":(0,1), "up":(-1,0), "down":(1,0)}
lines = []
testcases = 0
lineCount = 1
alienCount = 1
weights = 0

#graph creation
class Vertices:
    def __init__(self):
        self.vertices = list() #sets of (i,j) coordinates

    def find(self, i, j):
        if (i, j) in self.vertices:
            return True
        return False

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {} # keys with list of the edges with ther respective weights {key: [vertex 1, vertex 2, weight]}
    
    def addEdge(self,f,t, t1, w):
        if f not in self.graph:
            self.graph[f] = []
        
        self.graph[f].append((t, t1, w))

    def getEdges(self):
        return self.graph



# loops through all the input and returns aliens[(i,j)]   start(i,j)   visited[i][j] True or False for walls   and vertices ????? why here?
def getInfoFromMaze(x, y, visited, aliens, start, lineCount):

    vertices = Vertices()
    alienCount = 1

    for i in range(y):
        temp = list(lines[lineCount])
        for j in range(len(temp)):
            if(temp[j] == '#'):
                visited[i][j] = True
            if(temp[j] == 'S'):
                start = (i, j)
            if(temp[j] == 'A'):
                aliens.append((i, j))
                alienCount += 1
        lineCount += 1

    return vertices, aliens, start, lineCount, visited

# map functions for efficiency, having unions of edges to use instead of different paths involving the same edges
class UnionFind:
    def __init__(self):
        self.nodeMap = {}

    def getKeys(self):
        return list(self.nodeMap.keys())

class Node:
    def __init__(self, data, rank):
        self.data = data
        self.parent = 0
        self.rank = rank

def makeSet(data, rank, UnionFind):
    node = Node(data, rank)
    node.parent = node
    UnionFind.nodeMap[data] = node

def union(UnionFind, data1, data2):
    node1 = UnionFind.nodeMap[data1]
    node2 = UnionFind.nodeMap[data2]
    parent1 = findset(node1)
    parent2 = findset(node2)

    if(parent1.rank >= parent2.rank):
        if(parent1.rank == parent2.rank):
            parent1.rank += 1
            parent2.parent = parent1

        parent2.parent = parent1
    else:
        parent1.parent = parent2

def findset(node):
    node_parent = node.parent
    if(node == node_parent):
        return node_parent
    node_parent = findset(node_parent.parent)
    node.parent = node_parent
    return node_parent

# Creates a minimum spanning tree
def createMST(edges, temp, sizeofnodes):
    mst = []
    uf = UnionFind()
    for edge in temp:
        makeSet(edge, 0, uf)

    sortedEdges = sorted(edges, key= lambda item: item[1]) #creating unions between edge 0 -> edge 2 etc
    for edge in sortedEdges:
        if not findset(uf.nodeMap[edge[0]]) == findset(uf.nodeMap[edge[2]]):
            union(uf, edge[0], edge[2])
            mst.append(edge[1])
            if(len(mst) == sizeofnodes - 1):
                break
    return mst

# Dijkstra's Algorithm - Calculates shortest paths between nodes, uses heap for optimization ((E+V)logV where E=|edges| and V=|Vertices|)
def dijkstra(source, vertices, visited):
    temp = [row[:] for row in visited]
    inf = 9999
    dist = {x: inf for x in vertices}
    dist[source] = 0
    priorityQueue = []
    row = 0
    col = 0

    heapq.heappush(priorityQueue, [dist[source], source]) 

    while(priorityQueue):
        u = heapq.heappop(priorityQueue)
        u_dist = u[0]
        u_id = u[1]
        if u_dist == dist[u_id]:
            temp[u_id[0]][u_id[1]] = True
            for direct in directions.values():
                row = u_id[0] + direct[0]
                col = u_id[1] + direct[1]
                if(not temp[row][col]):
                    newNode = (row, col)
                    dist[newNode] = u_dist + 1
                    temp[row][col] = True
                    heapq.heappush(priorityQueue, [dist[newNode], newNode])

    return dist

def getDistances(startNode, toNodes, visited):
    dist = dijkstra(startNode, toNodes, visited)
    total = []
    for node in toNodes:
        total.append([startNode, dist[node], node])

    return total

def findAll(aliens, visited):
    edges = []
    while(len(aliens) > 1):
        temp = aliens[:1][0]
        aliens = aliens[1:]
        edges.extend(getDistances(temp, aliens, visited))
    return edges

lines = [line.rstrip('\n') for line in sys.stdin]
testcases = int(lines[0])
results = []

for i in range(testcases):

    data = list(map(int, lines[lineCount].split()))
    x = data[0]
    y = data[1]
    aliens = []
    start = 0
    graph = 0
    visited = [[False for i in range(x)] for j in range(y)]
    lineCount += 1

    vertices, aliens, start, lineCount, visited = getInfoFromMaze(x, y, visited, aliens, start, lineCount)
    aliens.insert(0, start)


    if(start == 0 or len(aliens) == 1):
        results.append(0)
        continue

    edges = []
    temp2 = aliens[:]
    while(len(aliens) > 1):
        temp = aliens[:1][0]
        aliens = aliens[1:]
        dist = dijkstra(temp, aliens, visited)
        for alien in aliens:
            edges.append([temp, dist[alien], alien])

    mst = createMST(edges, temp2, len(temp2))
    
    results.append(sum(mst))

for res in results:
    print(str(res))