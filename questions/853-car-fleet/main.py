from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        POS, TTT = 0, 1

        cars = []
        for i in range(len(speed)):
            p, s = position[i], speed[i]
            cars.append((p, (target - p) / s))
        
        cars.sort(key=lambda c: c[POS])
        fleets = []

        while cars:
            front_car = cars.pop()
            while not fleets or front_car[TTT] > fleets[-1][TTT]:
                fleets.append(front_car)

        return len(fleets)

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

print(Solution().carFleet(target, position, speed))