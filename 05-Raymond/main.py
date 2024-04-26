class Node:
    def __init__(self, name):
        self.name = name
        self.holder = None
        self.request_queue = []


# Tree
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")

E.holder = B
D.holder = B
B.holder = A
C.holder = A

nodes = [A, B, C, D, E]

# util functions
def get_node(name):
    for node in nodes:
        if node.name == name:
            return node
    return None

def request(name):
    # get node object
    node = get_node(name)
    
    # request holder nodes
    while node.holder is not None:
        print(f"{node.name} is requesting {node.holder.name}")
        node.holder.request_queue.append(node)
        node = node.holder

    # change the holder
    while node.request_queue.__len__() != 0:
        node.holder = node.request_queue.pop(0)
        print(f"{node.holder.name} is a root")
        node = node.holder
    
    # make root node point to None
    node.holder = None

def dispaly():
    print("Current tree: ")
    points = {}
    for node in nodes:
        if node.holder is not None:
            if node.holder.name not in points:
                points[node.holder.name] = []
            points[node.holder.name].append(node.name)
    print(points)

while(True):
    name = input("Enter requesting node: ")
    if not name:
        break
    request(name)
    dispaly()
    print()

# Enter requesting node: E
# E is requesting B
# B is requesting A
# B is a root
# E is a root
# Current tree: 
# {'B': ['A', 'D'], 'E': ['B'], 'A': ['C']}

# Enter requesting node: C
# C is requesting A
# A is requesting B
# B is requesting E
# B is a root
# A is a root
# C is a root
# Current tree: 
# {'C': ['A'], 'A': ['B'], 'B': ['D', 'E']}

# Enter requesting node:     