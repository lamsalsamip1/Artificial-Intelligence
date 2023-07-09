
def expand(node, graph):
  
    if node in graph.keys():
        return graph[node]
    return []


def DFS(start,goal,graph):

    #Initializing a stack
    stack=[start]
    reached=[start]
    
    

    #while queue is not empty
    while stack:
        node=stack.pop()
        for child in expand(node,graph):
            if child == goal:
                return [reached,child]
            if child not in reached:
                reached.append(child)
                stack.append(child)
    return False

graph ={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'F':['G'],
}

result = DFS('A','G',graph)
if result:
    print(f"The path is {'->'.join(result[0])}->{result[1]}")
else:
    print("No solution")