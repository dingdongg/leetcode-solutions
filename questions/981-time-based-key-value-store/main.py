from collections import defaultdict

'''specs:
- can store multiple values for the same key at different time stamps
-  retrieve the key's value at a certain timestamp.

timestamp A: "foo" -> "bar"
timestamp B: "foo" -> "baz"

TimeMap.get("foo", A) -> "bar"
TimeMap.get("foo", B) -> "baz"

if we assume that A <= B (and B <= C), and we call get("foo", C) -> return results for get("foo", B)
else, if "foo" doesn't exist at any timestamp, return ""

set():
- Stores the key key with the value value at the given time timestamp

get():
- Returns a value such that set was called previously
- timestamp_prev <= timestamp
- If there are multiple such values, it returns the value associated with the largest timestamp_prev
- If there are no values, it returns ""

CONSTRAINTS:
- key, value consist of lowercase english + digits
- timestamps of set() are STRICTLY INCREASING

INPUT
Init obj
set('foo', 'bar', 1)    # 1: foo -> bar
get('foo', 1)           # return bar
get('foo', 3)           # return bar 
set('foo', 'bar2', 4)   # 4: foo -> bar2
get('foo', 4)           # return bar2
get('foo', 5)           # return bar2

history of the value for "foo":
1: "bar"
4: "bar2"
5: "bar3"

1..n:

get("foo", k) where 1 <= k,

perform a binary search on the history of values of "foo" (based on timestamp)
if matching timestamp exists, return it
otherwise, timestamp is invalid (ie. entry doesn't exist) -> return "foo" with the latest timestamp


IMPLEMENTATION:
primary dictionary -> this will determine whether or not a given key exists at all 
- map strings to arrays of tuples in the format (value, timestamp)
- array will be sorted in non-decreasing order of the timestamp
- if entry doesn't exist in the array, return the rightmopst element in the arary (ie. the most rercent)
- otherwise, we have found the particular timestamp value - return it


when we call set(key, value, timestamp):
- we know that timestamps will be in strictly increasing order
- that means we can just append to the back of the array returned from the dictionary
- the array will still maintain its sorted property

...'''



class TimeMap:
    def __init__(self):
        self.primary_map = {} # maps to arrays of tuples in the format (value, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.primary_map:
            self.primary_map[key] = []

        self.primary_map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        # 3 cases:
        # a) entry doesn't exist at all -> return ""
        # b) entry exists, but timestamp doesn't -> return item in the array with a timestamp <= input timestamp
        # c) entry exists AND timestamp exists -> return that value

        if key not in self.primary_map: return ""

        # case b)
        items = self.primary_map[key]
        # perform binary search over items to find element where timestamp == timestamp
        l, r = 0, len(items)

        while l < r:
            m = (l + r) >> 1

            elm = items[m]
            if elm[1] == timestamp:
                # found target, return its value
                return elm[0]
            elif elm[1] < timestamp:
                l = m + 1
            elif elm[1] > timestamp: # discard right half
                r = m
        
        # by this point, the pointers will have converged at the index where the given timestamp value
        # WOULD be found, if it existed
        # since we want an item with a timstamp <= input timestamp,
        # return the item to the left of that pointer
        # case c)

        # l and r CAN converge outside of the array (due to my implenmentation of binary serarch)
        # [0, len(items)]

        if l == len(items): # converged outside, this means that we can just return rightmost element
            return items[-1][0]
        
        if l == 0:          # the only time we converge to 0 is if the timestamp is before all other timestamps
            return ""

        # otherwise,
        return items[l - 1][0] # in this case, the item immediately to the left of the pointer is the target we're looking for 
    

tm = TimeMap()

tm.set('foo', 'bar', 1)
print(tm.get('foo', 1))
print(tm.get('foo', 3))
tm.set('foo', 'bar2', 4)
print(tm.get('foo', 4))
print(tm.get('foo', 5))

# 10 20 30 <- 40
# ^     ^   ^

# 10 20 30 <- 28
#       ^^

# 10 20 30 <- 15
# ^  ^

# 10 20 30 <- 15
#    ^^

# 10 15 20 30

# 10 13 30 <- 15

# 10 20 30 <- 29

# 10 20 30 <- 2
# ^         ^

# 10 20 30 <- 2
# ^^

# 10 20 30 <- 11
# ^        ^

# 10 20 30 <- 11
#    ^^