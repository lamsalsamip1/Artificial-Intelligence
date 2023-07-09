
def expand(node, graph):
  
    if node in graph.keys():
        # print(graph[node].reverse())
        return graph[node]
    return []

def DFS(start,goal,graph):

    #Initializing a stack
    stack=[start]
    reached=[start]
    path=[]
    
    #while queue is not empty
    while stack:
        node=stack.pop()
        path.append(node)
        if node ==  goal:
            return path
        
        for child in expand(node,graph):
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

result = DFS('A','E',graph)
if result:
    print(f"The path is {'->'.join(result)}")
else:
    print("No solution")