# 844 - Backspace String Compare

## General Thoughts
- Easy, No tricks/"aha"s in the question.

## Things to note
- You can note the characters to "skip" by keeping count of the total backspaces seen.
- Whenever you reach a non-"#" character and the number of backspaces you encountered is `> 0`, decrement the count and skip that character
- do this for both strings and compare the post-processed strings

### Performance

*Time* - `O(len(s) + len(t))`, since you have to iterate through strings `s` and `t`

*Memory* - `O(max(len(s), len(t)))` for the buildup of the post-processed string

---

## Algorithm
```
1. Define a function, process(s), as follows:
    a. Initialize a pointer to the last index of string s
    b. Initialize the number of backspaces seen to 0
    c. Initialize the post-processed string variable
    d. While the pointer isn't out of bounds,
        a. if s[ptr] is "#", increment backspaces by 1
        b. otherwise, 
            a. if backspaces > 0, decrement backspaces by 1
            b. otherwise, add s[ptr] to the buildup string
        c. decrement ptr by 1
    e. return post-processed string
2. call process() on s
3. call process() on t
4. return the equality comparison between 2. and 3.
```

## Things I learned
- Thinking about the fact that the backspace character always came *after* the character to delete helped me realize that I should iterate in reverse order
- This problem seemed like it was categorized as "two-pointers" in the sense that there is 1 pointer to use for each of the two strings `s` and `t` 

## Things to improve
- This problem was pretty straightforward so I didn't notice any places where I messed up