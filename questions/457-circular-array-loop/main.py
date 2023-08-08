from typing import List

class Solution:
    # invalid cycles: 
    #   - cycles of length 1 (next_index(x) == x)
    #   - cycles that go in different directions (??)
    def circularArrayLoop(self, nums: List[int]) -> bool:  
        def next_index(ptr: int) -> int:
            added = ptr + nums[ptr]
            dividend = added if added >= 0 else len(nums) + added
            return dividend % len(nums)
        
        seen_nodes = set()

        for i in range(len(nums)):
            if i in seen_nodes: continue
            direction = 1 if nums[i] > 0 else -1
            slow = fast = i
            length = 0
            seen_nodes.add(slow)

            while slow != next_index(slow):
                if slow == fast and length > 1: return True
                slow = next_index(slow)
                length += 1
                if nums[next_index(fast)] * direction < 0: break
                seen_nodes.add(fast)
                fast = next_index(next_index(fast))
                if nums[fast] * direction < 0: break
                seen_nodes.add(fast)

        return False
            
s = Solution()
arr = [-1,-1,-3]
print(s.circularArrayLoop(arr))