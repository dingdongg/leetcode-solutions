# 146 - LRU Cache

## General Thoughts
- thinking through the use cases helped
- the choice of data structures was largely determined by the runtime performance rqeuirements
    - `O(1)` get() meant that we needed a DS with fast retrievals (which led to a map)
    - `O(1)` put() meant that we needed constant time removal of LRU + constant time inserts (which led to linked list - more specifically doubly linked list to re-arrange pointers easily)

## Things to note
- cannot use circular arrays as an alternative to linked lists
- if we access an existing cache entry, we have to move it to the front and shift all subsequent cache entries back by 1 slot - this is an `O(n)` operation
- we use *doubly* linked lists combined with a map. This allows constant time access to any node in the linked list, as well as its adjacent neighbor nodes (to re-arrange pointers in case of removals)

### Performance

*Time* - `O(1)` for both `get()` and `put()`

*Memory* - `O(capacity)`

---

## Algorithm
```
1. LRUCache(capacity)
    1. set size = 0, cap = capacity, cache = map(), head = tail = null
2. Get(key)
    1. if key is in cache,
        1. refresh(cache[key]) to update recency
        2. return cache[key].val
    2. otherwise, return -1
3. Put(key, value)
    1. if key is in cache,
        1. set cache[key].val = value
        2. refresh(cache[key]) to update recency
        3. return
    2. otherwise, set node = Node(key, value)
    3. if size == cap, remove(self.head) to make room
    4. append(node) to insert new node
4. Refresh(node)
    1. if node is null, return
    2. set node.next.prev = node.prev
    3. if node.prev is null, set head = node.next
    4. otherwise, set node.prev.next = node.next
    5. set node.prev = tail
    6. set tail.next = node
    7. set node.next = null
    8. set tail = node
5. Remove(node)
    1. if node is not null,
        1. set head = node.next
        2. if head is not null, set head.prev = None
        3. decrement size by 1
        4. delete cache[node.key]
7. Append(node)
    1. if node is not null,
        1. if tail is not null,
            1. set tail.next = node
            2. set node.prev = tail
        2. set tail = node
        3. if head is null, head = node
        4. increment size by 1
        5. set cache[node.key] = node
```

## Things I learned
- linked lists are good for keeping track of data access patterns! (ie. history of data access)

## Things to improve
- Maybe I didn't think through the problem hard enough, but I had to deal with a lot of *"what if this node is null"*, which got pretty annoying. The use of dummy nodes as seen in neetcode's vid seems to be a good workaround to this