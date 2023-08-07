# 876 - Middle of the Linked List

## General Thoughts
- Easy

## Things to note
- When you use the tortoise-hare method, the fast pointer is always twice the distance of the slow pointer. That means that when the fast pointer reaches the end of the linked list, the slow pointer will be at the halfpoint through the linked list

### Performance

*Time* - `O(n)`

*Memory* - `O(1)`

---

## Algorithm
```
1. Initialize slow and fast pointers to the head of the linked list
2. While fast and fast.next are defined,
    1. Increment slow pointer by 1
    2. Increment fast pointer by 2
3. Return slow pointer
```
## Things I learned
- Not much, the intuition for this problem came to me pretty quickly
- I guess this is one of the rare applications of tortoise-hare method that isn't concerned with cycles