from collections import deque
graph = {}
def add_node(v):
    if v in graph:
        print(v, "already exist in graph")
    else:
        graph[v] = []  

def add_edge(u, v):
    if u not in graph and v not in graph:
        print(u, "or", v, "is not present in graph")
    else:
        graph[u].append(v)
        graph[v].append(u)    

# graph traverse algorithm Depth First Search
def DFS(node, graph):
    if node not in graph:
        print("Node is not present in graph")
        return
    visited = set()
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)            

# graph traverse algorithm Breath First Search
def BFS(node, graph):
    if node not in graph:
        print("Node is not present in graph")
        return
    visited = set()
    myqueue = deque()
    myqueue.append(node)
    visited.add(node)
    while myqueue:
        current = myqueue.popleft()
        print(current)
        for itemNode in graph[current]:
            if not itemNode in visited:
                visited.add(itemNode)
                myqueue.append(itemNode)


add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_edge("A", "B")
add_edge("A", "C")
add_edge("A", "D")
add_edge("B", "E")
add_edge("B", "D")
add_edge("C", "D")
add_edge("D", "E")
BFS("A", graph)
