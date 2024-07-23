from typing import List

# O(log(m) * log(n)) --> for large enough values of m and n, this is the slower solution!
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         rl, rh = 0, len(matrix)

#         while rl < rh:
#             rm = (rl + rh) >> 1
#             cl, ch = 0, len(matrix[0])
            
#             while cl < ch:
#                 cm = (cl + ch) >> 1
#                 mid_cell = matrix[rm][cm]

#                 if mid_cell == target:
#                     return True
#                 elif mid_cell < target:
#                     cl = cm + 1
#                 else:
#                     ch = cm

#             if cl == 0:
#                 rh = rm
#             elif cl == len(matrix[0]):
#                 rl = rm + 1
#             else:
#                 return False
        
#         return False

# O(log(m) + log(n)) == O(log(mn)) (optimized version)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        rl, rh = 0, len(matrix)

        # do binary search along the rows to find the appropriate row to search
        while rl < rh:
            rm = (rl + rh) >> 1
            if matrix[rm][0] == target or matrix[rm][n - 1] == target:
                # edge case: target is at the start/end of a row
                return True
            elif matrix[rm][0] < target and target < matrix[rm][n - 1]:
                # target may be somewhere within this row
                rl = rm
                break
            elif matrix[rm][0] > target:
                # must search a previous row
                rh = rm
            elif matrix[rm][n - 1] < target:
                rl = rm + 1
                # must search a future row
        
        if rl >= rh: return False

        cl, ch = 0, len(matrix[0])
        row = matrix[rl]
        while cl < ch:
            cm = (cl + ch) >> 1
            mid_cell = row[cm]

            if mid_cell == target:
                return True
            elif mid_cell < target:
                cl = cm + 1
            else:
                ch = cm
        
        return False
    
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

print(Solution().searchMatrix(matrix, target))