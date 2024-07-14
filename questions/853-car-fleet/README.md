# 853 - Car Fleet

## General Thoughts
- straightforward (mainly bc i solved this before lol)

## Things to note
- the important pieces for each car are:
    - its starting position (used as the key when sorting the array)
    - time it takes to reach `target` miles
        - if this value is less than that of the fleet in front of it, it will join the fleet
        - this is key in counting up the total number of fleets that arrive at the destination
- by definition, the car at the very front always forms a fleet
- by sorting the cars by position, we can pop from the back to determine the cars that join the
current fleet of interest
- otherwise, we can push to a stack of fleets and repeat the process
    - **thus, `fleets` will be a monotonically increasing stack on arrival times**
    - **`cars` will be a monotonically increasing stack on starting position**

### Performance

*Time* - `O(n log n)` b/c we had to sort an array

*Memory* - `O(n)`, to hold the stack of fleets and cars

---

## Algorithm
```
1. init two empty stacks, `fleets` and `cars`
2. for i in range(len(speed)),  
    1. set p, s = position[i], speed[i]
    2. cars.push((p, (target - p) / s))
3. sort cars in ascending order of position
4. while cars isn't empty,
    1. set front_car = cars.pop()
    2. while fleets is empty or front_car's arrival time > fleet[-1]'s arrival time,
        1. fleets.push(front_car)
5. return length of fleets
```

## Things I learned
- good places to start understanding the problem are the most intuitive drawings of the problem
- in this case, it was a line graph of distance over time
- from the drawings, figure out the assumptions you were operating on top of
    - + any data structures that allow you to solve the problem within the constraints
    of runtime/memory performance requirements

## Things to improve
- still not comfortable with stacks