
def expand(node, graph):
  
    if node in graph.keys():
        return graph[node]
    return []


def BFS(start,goal,graph):

    #Initializing a queue
    frontier=[start]
    reached=[start]
    
    

    #while queue is not empty
    while frontier:
        node=frontier.pop(0)
        for child in expand(node,graph):
            if child ==  goal:
                return [reached,child]
            if child not in reached:
                reached.append(child)
                frontier.append(child)
    return False

graph ={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'F':['G'],
}

result = BFS('A','G',graph)
if result:
    print(f"The path is {'->'.join(result[0])}->{result[1]}")
else:
    print("No solution")