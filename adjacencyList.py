graph = {}
def add_node(v):
    if v in graph:
        print(v, "already exist in graph")
    else:
        graph[v] = []  

def add_edge(u, v, cost=1):
    if u not in graph and v not in graph:
        print(u, "or", v, "is not present in graph")
    else:
        graph[u].append([v, cost])
        graph[v].append([u, cost])    

add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_edge("A", "B", 3)
add_edge("A", "C", 4)
add_edge("A", "D", 7)
add_edge("B", "E")
add_edge("B", "D")
add_edge("C", "D")
add_edge("D", "E", 5)
print(graph)
