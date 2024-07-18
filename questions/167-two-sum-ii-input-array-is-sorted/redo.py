from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(1) memory => can only use counter/pointer variables - no other collection data structures
        # for each item in the numbers array,
        # - we can calculate the "other number" to look for (target - numbers[i])
        # - because the array is sorted, if we iterate from left to right,
        #   the "other number" will always be bigger than numbers[i]
        #   - hence, we can look at all the items in the right side of numbers[i]
        #     and perform a binary search for that "other number"
        # - with the naive solution, the runtime is O(n^2) - this is because of a 
        #   linear serarch thorugh the array for every n item in the list

        l, r = 0, len(numbers) - 1

        while l < r:
            summed = numbers[l] + numbers[r]
            if summed > target:
                r -= 1
            elif summed < target:
                l += 1
            else:
                return [l + 1, r + 1]
        
        return [-1, -1]
    
# numbers = [2,3,4]
numbers = [2,7,11,15]
target = 9
print(Solution().twoSum(numbers, target))
