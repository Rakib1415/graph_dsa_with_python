# add node in 2d matrix
def add_node(v):
    global nodes_count
    if v in nodes:
        print(v, "is already exist in graph")
    else:
        nodes_count = nodes_count + 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = [0]*nodes_count
        graph.append(temp)    

# add connection between two adjacency nodes u and v
def add_edge(u, v, cost=1):
    if u in nodes and v in nodes:
        u_index = nodes.index(u)
        v_index = nodes.index(v)
        graph[u_index][v_index] = cost
        graph[v_index][u_index] = cost
    else:
        print(u, "or", v, "not present in graph")

def print_graph():
    for i in range(nodes_count):
        for j in range(nodes_count):
            print(graph[i][j], end=" ")
        print()    


nodes_count = 0
nodes = []
graph = []

add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_edge("A", "B", 4)
add_edge("A", "C")
add_edge("A", "D")
add_edge("B", "E")
add_edge("B", "D")
add_edge("C", "D")
add_edge("D", "E", 7)
print_graph()
