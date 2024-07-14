from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        HGHT, IDX = 0, 1
        bars = []
        max_area = -1

        for i in range(len(heights)):
            if not bars or bars[-1][HGHT] < heights[i]:
                # if the current bar height is greater than the previous tallest bar,
                # add this bar to the bars stack
                bars.append((heights[i], i))
            elif bars and bars[-1][HGHT] == heights[i]:
                # adding bars of equal heights is redundant,
                # because we already have indexes which we can
                # use to calculate bar widths. (and hence count # of equal-height bars)
                continue
            else:
                new_width = 0
                while bars and bars[-1][HGHT] >= heights[i]:
                    # while the current bar height is <= the rightmost bar height,
                    # try calculating 2 possible areas and update max_area accordingly
                    # also use `width` to set new_width, in case we are dealing with
                    # bars with widths > 1
                    b = bars.pop()
                    width = i - b[IDX]
                    new_width = width
                    area1 = width * b[HGHT]
                    area2 = (width + 1) * heights[i]
                    max_area = max(area1, area2, max_area)
                # using new_width, we can portray that the rightmost tallest bar
                # consists of a width >1
                bars.append((heights[i], i - new_width))
        
        while bars:
            # for every bar left over, pop them from the stack and 
            # calculate possible areas
            b = bars.pop()
            w = i + 1 - b[IDX]
            max_area = max(w * b[HGHT], max_area)
                
        return max_area

    
heights = [3,6,5,7,4,8,1,0] 
print(Solution().largestRectangleArea(heights))