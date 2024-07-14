from typing import Optional
from collections import defaultdict

class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.size = 0
        self.cap = capacity
        self.cache = defaultdict()
        self.head = self.tail = None
        print(f"LRUCache(cap={self.cap})")
    
    def state(self):
        curr = self.head
        log = "State: "
        while curr:
            log += f"({curr.key}, {curr.val}) -> "
            curr = curr.next
        print(log)

    def get(self, key: int) -> int:
        print(f"-----\nget({key})")
        if key in self.cache:
            # update node recency
            self.refresh(self.cache[key])
            print(f"get({key}) = {self.cache[key].val}")
            return self.cache[key].val
        
        print(f"get({key}) = -1")
        return -1
        
    def put(self, key: int, value: int) -> None:
        print(f"-----\nput({key}, {value})")
        if key in self.cache:
            print(f"replace {self.cache[key].val} -> {value}")
            self.cache[key].val = value
            self.refresh(self.cache[key])
            return
        
        node = Node(key, value)
        if self.size == self.cap: 
            self.remove(self.head)
        self.append(node)

    def remove(self, node: Optional[Node]) -> None:
        if node != None:
            print(f"remove({node.key}, {node.val})")
            self.head = node.next
            if self.head != None:
                self.head.prev = None
            self.size -= 1
            del self.cache[node.key]
        else:
            print("remove() - node is none!")

    def append(self, node: Optional[Node]) -> None:
        if node != None:
            print(f"append({node.key}, {node.val})")
            if self.tail != None:
                self.tail.next = node
                node.prev = self.tail
            self.tail = node
            if self.head == None: self.head = node
            self.size += 1
            self.cache[node.key] = node
        else:
            print("append() - node is none!")

    def refresh(self, node: Node) -> None:
        print(f"refresh({node.key}, {node.val})")
        if node.next == None: return
        
        node.next.prev = node.prev
        if node.prev == None:
            self.head = node.next
        else:
            node.prev.next = node.next
        
        node.prev = self.tail
        self.tail.next = node
        node.next = None
        self.tail = node

commands = ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
args = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]

obj = None

outputs = []

for i in range(len(commands)):
    c, a = commands[i], args[i]
    res = None
    if c == "LRUCache":
        obj = LRUCache(a[0])
    elif c == "put":
        obj.put(a[0], a[1])
    elif c == "get":
        res = obj.get(a[0])
    outputs.append(res)
    obj.state()

print(outputs)