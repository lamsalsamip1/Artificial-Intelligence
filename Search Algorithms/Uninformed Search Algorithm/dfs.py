## Implementation of  DEPTH FIRST SEARCH

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        
    
class StackFrontier():
    def __init__(self):
        self.stack = []

    # Add an element
    def add(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack) == 0
    # Remove an element
    def pop(self):
        if self.is_empty():
            return None
        node = self.stack[-1]
        self.stack = self.stack[:-1]
        return node

    def top(self):
        if self.is_empty():
            return None
        return self.stack[0]
    
    def contains_state(self, state):
        return any(node.state == state for node in self.stack)
    

def depth_first_search(initial,goal):

    explored=set()
    num_explored=0

    #Keep starting node in the frontier
    start =Node(state=initial,parent=None,action=None)
    frontier=StackFrontier()
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
            return actions,states,num_explored
        
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

path,locations,num_exp = depth_first_search("Samakhushi","Lazimpat")
print(f"The path to take is :")
for item in path:
    print(f"-{item}",end="")
print("")
for item in locations:
    print(f"-{item}",end="")
print(f"\nNumber of states explored:{num_exp}")
