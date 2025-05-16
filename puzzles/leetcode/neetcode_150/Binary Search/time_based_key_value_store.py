"""
Pretty straightforward no real tricky edge cases which I needed to think
through, there was a small thing where the problem specified that we should
return the first instance we encounter a value smaller than timestamp, and
if there are none, then we should return a empty string
"""

class TimeMap:

    def __init__(self):
        self.contents = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.contents:
            self.contents[key].append((value, timestamp))
        else:
            self.contents[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.contents:
            return ""

        
        # get nearest by performing a binary search
        arr = self.contents[key]
        l, r = 0, len(arr)-1

        if timestamp < arr[0][1]:
            return ""

        while l <= r:
            m = (r-l)//2 + l

            if arr[m][1] == timestamp:
                return arr[m][0]
            elif arr[m][1] < timestamp:
                l = m + 1
            else:
                r = m - 1
        
        return arr[r][0]