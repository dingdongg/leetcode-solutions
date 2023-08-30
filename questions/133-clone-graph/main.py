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
    
    def toStr(self):
        ret = f"Node(val = ${self.val})\n"
        for i, n in enumerate(self.neighbors):
            ret += f"  -> Node(val = ${n.val})\n"
        return ret

class Queue:
    def __init__(self, items: list = []):
        self.backView = []
        self.frontView = []
        for i in items: self.push(i)

    def __len__(self):
        return len(self.backView) + len(self.frontView)

    def push(self, val: any):
        self.backView.append(val)
    
    def pop(self) -> any:
        if self.isEmpty(): return
        if not self.frontView:
            while self.backView: self.frontView.append(self.backView.pop())
        return self.frontView.pop()
    
    def peekBack(self) -> any:
        if self.isEmpty(): return
        if not self.backView: return self.frontView[0]
        return self.backView[-1]

    def peekFront(self) -> any:
        if self.isEmpty(): return
        if not self.frontView: return self.backView[0]
        return self.frontView[-1]

    def isEmpty(self) -> bool:
        return len(self) == 0

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None: return None
        newGraph = Node(node.val, node.neighbors)
        created_nodes = {}
        created_nodes[node.val] = newGraph

        q = Queue([newGraph])

        while not q.isEmpty():
            newNode = q.pop()
            newNeighbors = []

            for ngh in newNode.neighbors:
                newNeighbor = created_nodes.get(ngh.val, Node(ngh.val, ngh.neighbors))
                newNeighbors.append(newNeighbor)
    
                if ngh.val not in created_nodes: 
                    q.push(newNeighbor)
                    created_nodes[ngh.val] = newNeighbor

            newNode.neighbors = newNeighbors
        
        return newGraph


adjacencies = [[2,4],[1,3],[2,4],[1,3]]
# adjacencies = [
#     [2],
#     [1, 3, 4],
#     [2],
#     [2, 5, 6, 7],
#     [4],
#     [4, 7],
#     [4, 6, 8, 9],
#     [7],
#     [7],
# ]
s = Solution()
nodes = []
for i, a in enumerate(adjacencies):
    nodes.append(Node(i + 1))

for i, a in enumerate(adjacencies):
    for n in a: nodes[i].neighbors.append(nodes[n - 1])

def traverse(node: Node):
    if node.val not in seen:
        seen.add(node.val)
        print(node)
        for n in node.neighbors:
            traverse(n)

# traverse(nodes[0])

# print("--------")

seen = set()

newGraph = s.cloneGraph(nodes[0])
# traverse(newGraph)

def check(node: Node):
    if node.val not in seen:
        seen.add(node.val)
        # print(node.toStr(), nodes[node.val - 1].toStr())
        # print(f"{node.val}:", id(node), id(nodes[node.val - 1]), id(node) - id(nodes[node.val - 1]))
        for n in node.neighbors: print(f"node #{node.val} @{id(node)} -> node #{n.val} @{id(n)}")
        for n in node.neighbors: check(n)

check(newGraph)
