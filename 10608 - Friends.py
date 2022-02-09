
""" adding an edge to the given graph or a vertex if no vertex yet created with that edge """
def addEdge(graph, edge):
    edge = set(edge)
    (vrtx1, vrtx2) = tuple(edge)
    
    if vrtx1 in graph.keys():
        if vrtx2 not in graph[vrtx1]:
            graph[vrtx1].append(vrtx2)
    else:
        graph[vrtx1] = [vrtx2]

    if vrtx2 not in graph.keys():
            graph[vrtx2] = [vrtx1]

    if vrtx2 in graph.keys() and vrtx1 not in graph[vrtx2]:
        graph[vrtx2].append(vrtx1)

""" Depth First Search (non-recursive)"""
def DFS(graph, start):
    
    visited = set()
    stack = [start]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            stack.extend([x for x in graph[v] if x not in visited])
        
    return visited


cases = int(input())
i = 0
case_results = []

while i<cases:

    j=0
    towninfo = input().split()
    people =  int(towninfo[0])
    pairs = int(towninfo[1])
    town = {}

    while j < pairs: 
        pair = input().split()
        a = int(pair[0])
        b = int(pair[1])

        addEdge(town, {a,b})
        j += 1

    all_paths = []

    for start_vrtx in town.keys():
        all_paths.append(DFS(town, start_vrtx))

    if len(all_paths) > 0:
        max_len = max(len(p) for p in all_paths)
        case_results.append(max_len)
    elif len(all_paths) == 0: # if only single people
        case_results.append(1) #only friend groups of length 1

    i += 1 #flytta sen

for result in case_results:
    print(str(result))