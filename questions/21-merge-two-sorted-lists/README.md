# 21 - Merge Two Sorted Lists

## General Thoughts
- Pretty straightforward, hardest part was figuring out how to manipulate the pointers which wasn't too bad

## Things to note
- The key is to choose a starting list such that it has a smaller value than the other head
    - Afterwards, all you need to do is compare 2 values at each step:
        1. the other head
        2. the current head's next node
    - Simply point the current node's next pointer to the node with the smaller value
        - if you have to point to the other head, make sure to set `jump` to the current head's old next node and then update the other head to be at the jump pointer to not lose it

### Performance

*Time* - `O(n + m)`, the length of both lists combined 

*Memory* - `O(1)`, just a few pointer variables required

---

## Algorithm
```
1. If list1 is empty, return list2
2. If list2 is empty, return list1
3. Init curr and ret pointers to list2 if list2.val <= list1.val, or list1 otherwise
4. Init other_next pointer to list2 if list2.val > list1.val, or list1 otherwise
5. While curr is defined, 
    1. Set jump pointer to curr.next
    2. If jump is defined,
        1. If jump.val > other_next.val,
            1. Set curr.next to other_next
            2. Set other_next to jump
        2. Increment curr by 1
    3. Otherwise, set curr.next to other_next and break the loop
6. Return ret
```
## Things I learned
- It didn't feel like there was much of a formal "algorithm" being used, just pointer manipulations

## Things to improve
- I need to get better at fleshing out edge cases. 
    - For this problem, I thought of too many unnecessary edge cases that were covered by the main loop
        - tbf I guess it's better safe than sorry?
    - I think this problem arose because I didn't analyze the problem fully to draw out meaningful facts to use in designing my code
    - SOLUTION: analyze the problem more to draw out meaningful facts