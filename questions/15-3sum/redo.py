from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # naive: O(n^3) - brute force all triplets
        # better: for each number nums[i] in nums, we need to find 
        # two more numbers such that nums[i] + first + second == 0
        # we know nums[i], thus first + second == -nums[i]
        # this last sentence describes a problem we solved before - two sum II (sorted input array)
        # this will allow us to grab the pair of numbers in O(n) time, 
        # totalling to a runtime complexity of O(n^2) overall
        res = []
        nums.sort()
        prev = nums[0]
        i = 0

        while i < len(nums):
            target = nums[i] * -1
            pairs = self.twoSum(nums, i + 1, target)
            for p in pairs:
                res.append([nums[i], nums[p[0]], nums[p[1]]])

            prev = nums[i]
            # this will ensure that the triplets being added are unique
            while i < len(nums) and nums[i] == prev:
                i += 1
                
        return res

        
    # O(n) to grab all possible soluitions
    def twoSum(self, nums: List[int], start: int, target: int) -> List[List[int]]:
        res = []

        l, r = start, len(nums) - 1
        while l < r:
            summed = nums[l] + nums[r]
            if summed > target:
                r -= 1
            elif summed < target:
                l += 1
            else:
                res.append([l, r])
                # increment l while it is the same as its prev value
                # you could instead decrement r - it doesn't matter logically
                # proof:
                # - there are 2 possible cases at this point in the if statement:
                #       1. increment l
                #       2. decrement r
                # - given that nums[l] + nums[r] == target rn, if we do step 1,
                # - then on the next step we will have to decrement r.
                # - likewise, if we do step 2, the sum < target so we have to increment l
                # - thus, we end up at the same state with either step
                l += 1
                while l < r and nums[l - 1] == nums[l]: l += 1 # ensure unique pairs

        return res
    
nums = [-1,0,1,2,-1,-4]

print(Solution().threeSum(nums))