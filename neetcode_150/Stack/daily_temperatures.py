"""
This is a tricky one.

As we iterate through the array we can record the temperatures
as we see them, keeping the coldest temperature on the top of the array.

As soon as we encounter a warmer temp, we can pop until we fill in all those
colder days.

This popping process only happens once pet day
"""
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        ans = [0 for _ in range(len(temperatures))]
        for idx, temp in enumerate(temperatures):
            
            while stack and temp > stack[-1][1]:
                (day, day_temp) = stack.pop(-1)
                ans[day] = idx - day
            
            stack.append((idx, temp))

        return ans