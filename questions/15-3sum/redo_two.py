from typing import List

"""

given an int array `nums`, return ALL tripets [nums[i], nums[j], nums[k]] 
such that:
- i != j != k
- triplet sum == 0

NO DUPLICATE TRIPLETS ALLOWED IN SOLUTION SET


ex1
nums = [-1,0,1,2,-1,-4]

-1 -> need to find two numbers taht sum to 1
    -> if i do naive way (ie. two sum I), i do O(n) work using O(n) space
        - in total, this will be O(n^2)
    -> if i do two sum II, i must first sort the list; O(n log n)
        - then, I do O(n) work with constant space 
        - in total, this is still O(n^2)
    
        both solutions yield O(n^2) runtime overall, but second option
        has a more mild memory usage so we will roll with that

[-4 -1 -1 0 1 2]

-4 -> twoSumII([-4 -1 -1 0 1 2], 4) -> []
-1 -> twoSumII([-4 -1 -1 0 1 2], 1) -> [-1 0 1], [-1 -1 2]
 0 -> twoSumII([-4 -1 -1 0 1 2], 0) -> 
 1 -> twoSumII([-4 -1 -1 0 1 2], -1)
 2 -> twoSumII([-4 -1 -1 0 1 2], -2)


-1
    -1 -1
        -1 -1 0
        -1 -1 1
        -1 -1 2
    -1 0
        -1 0 1
        -1 0 2
    -1 1
        -1 1 2

...



this is the for loop associated with generating the above seuqence of triplets:
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            ...

we do this to avoid most of the duplciate triplets
- we can do the same with our current solution



"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        seen = set()
        i = 0
        
        while i < len(nums):
            num = nums[i]
            target = -num
            pairs = self.findPairs(nums, target, i + 1)

            for p in pairs: 
                triplet = [nums[i], nums[p[0]], nums[p[1]]]
                key = tuple(triplet)
                if key not in seen:
                    seen.add(key)
                    ret.append(triplet)

            i += 1
            while i < len(nums) and nums[i] == num: i += 1

        return ret

    def findPairs(self, nums: List[int], target: int, start: int) -> List[int]:
        ret = []
        l, r = start, len(nums) - 1

        while l < r:
            curr_sum = nums[l] + nums[r]

            if curr_sum < target: l += 1
            elif curr_sum > target: r -= 1
            else:
                ret.append([l, r])
                r -= 1
        
        return ret
    
nums = [0, 0, 0,0]
print(Solution().threeSum(nums))