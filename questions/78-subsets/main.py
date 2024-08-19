from typing import List

"""int array of UNIQUE elements, return ALL POSSIBLE subsets


each element in the array can either be included or not included in the array - 2 options
for n elements, this will generate 2^n subsets

we can think of a decision tree, where each level `i` will enumerate the possible sets
after considering the addition of nums[i] to the previously computed subsets up to `i-1`

start with an empty set, then:
- recursively compute the sets possible after adding nums[i]
- recursively compute the sets possible after NOT adding nums[i]
- DFS + backtracking will work
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def dfs(state: List[int], i: int):
            if i == len(nums):
                ret.append(list(state))
                return

            # consider adding nums[i]
            state.append(nums[i])
            dfs(state, i + 1)

            state.pop()
            dfs(state, i + 1)
        
        dfs([], 0)
        return ret

sets = Solution().subsets([1, 2, 3])

print(sets)
