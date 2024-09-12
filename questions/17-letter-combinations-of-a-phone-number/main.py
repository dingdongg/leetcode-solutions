from typing import List


"""

given string that contains digits in the range [2, 9], 
return all letter combinations that the number could rep
(any order is fine)

(0, 1 do not map to any letters)
2 - abc  (0-2)
3 - def  (3-5)
4 - ghi  (6-8)
5 - jkl  (9-11)
6 - mno  (12-14)
7 - pqrs (15-18)
8 - tuv  (19-21)
9 - wxyz (22-25)

ex1: "23"
- ad
- ae
- af
- bd
- be
- bf
- cd
- ce
- cf

[]
-> [a]
    -> [a d]
    -> [a e]
    -> [a f]
-> [b]
    -> [b d]
    -> [b e]
    -> [b f]
-> [c]
    -> [c d]
    -> [c e]
    -> [c f]

we are interested in finding all of the leaf nodes in this decision tree
- there will be O(2^n) of them, depending on the digits actually chosen

maximum memory usage will be the max length of the call stack, which is 
the height of the decision tree -> O(len(digits))

as we traverse the tree down from the root to leaf, we can keep track
of the letters in our path
- once we reach a leaf node, we can copy this sequence over into our solution set

"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []

        combos = []

        digit_to_letters = {}
        # prep work: create a dictionary mapping each digit to its characters

        digit_to_letters["2"] = ["a", "b", "c"]
        digit_to_letters["3"] = ['d', 'e', 'f']
        digit_to_letters["4"] = ["g", "h", "i"]
        digit_to_letters["5"] = ["j", "k", "l"]
        digit_to_letters["6"] = ["m", "n", "o"]
        digit_to_letters["7"] = ["p", "q", "r", "s"]
        digit_to_letters["8"] = ["t", "u", "v"]
        digit_to_letters["9"] = ["w", "x", "y", "z"]

        def solve(seq: List[str], i: int):
            # i is the index into the digits string
            # seq is the path so far 
            if i == len(digits):
                # sequence must be full, append to combos
                combos.append("".join(seq))
                return

            # otherwise, we are not at a leaf node; continue DFS traversal
            # for every letter mapped from the digit, call a dfs traversal on it after pushing to stack
            letters = digit_to_letters[digits[i]]
            for l in letters:
                seq.append(l)
                solve(seq, i + 1)
                seq.pop()

        solve([], 0)

        return combos
    
print(Solution().letterCombinations("32"))