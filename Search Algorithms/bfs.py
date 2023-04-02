class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        
    
class QueueFrontier():
    def __init__(self):
        self.queue = []

    # Add an element
    def add(self, item):
        self.queue.append(item)

    def is_empty(self):
        if len(self.queue)<1:
            return True
        return False

    # Remove an element
    def pop(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def top(self):
        if self.is_empty():
            return None
        return self.queue[0]
    
    def contains_state(self, state):
        return any(node.state == state for node in self.queue)
    

def breadth_first_search(initial,goal):

    explored=set()
    num_explored=0

    #Keep starting node in the frontier
    start =Node(state=initial,parent=None,action=None)
    frontier=QueueFrontier()
    frontier.add(start)
    
    while True:
        if frontier.is_empty():
                raise Exception("No solution")
        
        #remove element from frontier
        node = frontier.pop()
        num_explored += 1
        print(f"Current state:{node.state}|Goal={goal}")
        #Check if goal state is reached
        if node.state==goal:
            actions=[]
            states=[]
            while node.parent is not None:
                 actions.append(node.action)
                 states.append(node.state)
                 node = node.parent
            actions.reverse()
            states.reverse()
            return actions,states
        
        #Add the node to the set of explored nodes
        explored.add(node)

        #Add the child nodes to frontier
        if(node.state in graph):
            for action,state in  graph[node.state].items():
                # print(action,state)
                if not frontier.contains_state(state) and state not in explored:
                    child=Node(state=state,parent=node,action=action)
                    frontier.add(child)


#           Samakhushi
#          /           \
#     Thamel            Maharajgunj
#     /    \               /       \
# New Road  Lazimpat   Baluwatar  Budhanilkantha



graph={
    "Samakhushi":{"Left":"Thamel","Right":"Maharajgunj"},
    "Thamel":{"Left":"New Road","Right":"Lazimpat"},
    "Maharajgunj":{"Left":"Baluwatar","Right":"Budhanilkantha"}
}

path,locations = breadth_first_search("Samakhushi","Lazimpat")
print(f"The path to take is :")
for item in path:
    print(f"-{item}",end="")
print("")
for item in locations:
    print(f"-{item}",end="")