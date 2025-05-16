"""
This one was not so bad I think some of the stack practice helped!

Basically my approach was sort by position (because that is a big part of
causing these traffic jams), then compute the finishing time of the cars.

If the car behind is going to finish before the car in front, then just merge
the two cars together

(here i think it makes sense to traverse the array backwards)
"""
class Solution:
    def finish_time(self, target, position, speed) -> float:
        distance_to_travel = target - position
        return distance_to_travel/speed

    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = list(zip(position, speed))
        cars = list(sorted(cars, key=lambda x: x[0]))

        fleets = []
        for (position, speed) in reversed(cars):

            # if it will catch the car in front of it
            curr_finish_time = self.finish_time(target, position, speed)

            if not fleets:
                fleets.append(curr_finish_time)
                continue

            front_finish_time = fleets[-1]

            if curr_finish_time <= front_finish_time:
                pass 
            else:
                fleets.append(curr_finish_time)
        
        return len(fleets)
