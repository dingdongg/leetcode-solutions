from typing import List

"""

array of ints `numbers` sorted in non-decreasing order
find two numbers that add up to a `target`

indexes i and j of such two numbers must not be equal to each other
- return the 1-indexed values

CONSTRAINTS
- exactly one solution
- only use O(1) memory 


ex1
[2 7 11 15], target = 9
-> [1 2] since numbers at index 0 & 1 will add up to 9



memory constraint means taht we cannot use any other data structures
- no arrays, dictionaries, etc.
- our options are to use a couple of variables

naive way:
- iterate over all possible pairs and see if their sums add up to target
- O(n^2), constant memory

however, we know the input is sorted
- we can make use of a more efficient search algorithm than linear search
- => binary search

given a number at index i, we can figure out the corresponding other nubmer
we must find in order to complete the sum
num = numbers[i], other_num = target - num

we are given a collection of sorted numbers and the number we want to find
if numbers[i] > other_num,
- other number will be on the left; perform binary serach from index 0 to i-1
if numbers[i] < other_num,
- other number will be on the right; perform binary search from index i+1 to len(numbers)
if numbers[i] == other_num,
- look on the right side of numbers[i], since we will skip all redundant numbers ion oour algorithm

[2 7 11 15], target = 9

2 -> 7; perform binary serach on [7 11 15]
- target found, return

7 -> 2; perform binary seearch on [2]

11 -> -2; perform binary serach on [2 7]

15 -> -6; perform binary serach on [2 7 11]

runtime: O(n log n)
memory: O(1)



alternative idea:
- maintain two pointers, starting at the left and right ends of the list
- if the sum of the elements pointed to by the current pointers > target,
    - decrement the right pointer until it is no loonger equal to its previous value
- if the sum of the elements pointed to by the current pointers < target,
    - increment the left pointer until it is no longer equal to its previous value
- if the sum of the elements == target,
    - return the two indexes

    O(n) runtime complexity, O(1) memory usage
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum < target: left += 1
            elif curr_sum > target: right -= 1
            else: return [left + 1, right + 1]
            
numbers = [2,7,11,15]
target = 9

print(Solution().twoSum(numbers, target))