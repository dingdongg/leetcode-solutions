"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

"""

given reference to node in CONNECTED + UNDIRECTED graph,
return deep copy of graph

CONNECTED
= all nodes are reachable 

nodes contain a value + adjacency list of neighbors


we will have to traverse every node of the graph and create a deep clone of it
- need a set to keep track of visited nodes so we don't clone the same node more than once
- queue required to implement BFS

because graph is undirected, whenever we create an edge from A to B,
we must make sure to also create an edge going from B to A
- by traversing from A -> B -> A, i should end up at the same node instance (WRT memory layout)
- we can fetch already-created nodes by storing them in another data structure
    - best to index by nodes by their values, so dictionary will be good

with every node dequeued,
- store a reference to the node in the dictionary (node.val -> cloned node)
- mark node as visited
- for every neighbor in its adjacency list,
    - if the node does not exist in the dictionary, 
        - queue it up for traversal
    - create an edge from this node to that node (and vice versa)

the first time we clone a node and store it in the dictionary, it will have 0 neighbor references
(call this node A)
- in the next iteration, we will be traversing one of A's neighbors
    - A will have been initialized in the dictionary, allowing us to connect this node to node A
    - thus, an edge has been successfully cloned
    - this will extend to all neighbors of A (and more generally, any node in a graph)

the dictionary can act as a set that keeps track of already visited nodes, so it 
seems like there is no need for another set data structure

- queue
- dictionary (value -> cloned node OR None)
"""



from typing import Optional
from collections import defaultdict

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None 

        cloned_nodes = defaultdict(None)
        queue = []

        # clone root node
        cloned_parent = Node(val=node.val)
        queue.append(cloned_parent)
        cloned_nodes[node.val] = (cloned_parent, node.neighbors)

        while len(queue) > 0:
            curr_node = queue.pop(0)
            
            # iterate through neighbors to clone
            for neighbor in cloned_nodes[curr_node.val][1]:
                if neighbor.val not in cloned_nodes:
                    new_node = Node(neighbor.val)
                    cloned_nodes[neighbor.val] = (new_node, neighbor.neighbors)
                    # new_node.neighbors.append(curr_node)
                    queue.append(cloned_nodes[neighbor.val][0])
                curr_node.neighbors.append(cloned_nodes[neighbor.val][0])

            # problem: need to itereate children, but don't have access to the 
            #          original node's children list!
            #          -> store it together in the appropriate dict KV pair
        
        return cloned_parent

node_one = Node(1)
node_two = Node(2)
node_three = Node(3)
node_four = Node(4)

node_one.neighbors = [node_two, node_four]
node_two.neighbors = [node_one, node_three]
node_three.neighbors = [node_two, node_four]
node_four.neighbors = [node_one, node_three]

ret = Solution().cloneGraph(node_one)

queue = [ret]
seen = set()

while len(queue) > 0:
    node = queue.pop(0)

    if node.val not in seen:
        seen.add(node.val)

        queue += node.neighbors
        print(node.val)
        print(list(map(lambda n: n.val, node.neighbors)))