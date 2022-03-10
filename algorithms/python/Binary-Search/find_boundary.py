from typing import List

def find_boundary(arr: List[bool]) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index

if __name__ == '__main__':
    arr = [False, False, False, False, True, True, True]
    res = find_boundary(arr)
    print(res, "[expected] 4")
