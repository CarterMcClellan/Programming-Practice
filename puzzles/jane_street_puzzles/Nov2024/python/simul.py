from random import random
from tqdm import tqdm

def coord():
    return (random(), random())


"""
Square is 1x1

Distance to left: x - 0 = x
Distance to right: 1 - x
Distance to bottom: y - 0 = y
Distance to top: 1 - y
"""

left_key, right_key, bottom_key, top_key = "left", "right", "bottom", "top"

left_side_distance = lambda p: (p[0], left_key)
right_side_distance = lambda p: (1 - p[0], right_key)
bottom_side_distance = lambda p: (p[1], bottom_key)
top_side_distance = lambda p: (1 - p[1], top_key)
key_to_distance = {
    left_key: left_side_distance,
    right_key: right_side_distance,
    bottom_key: bottom_side_distance,
    top_key: top_side_distance,
}


def nearest_side(p) -> tuple[float, str]:
    """
    point (x, y) is a tuple
    """
    distance = []
    for key, distance_fn in key_to_distance.items():
        distance.append((distance_fn(p), key))

    return min(distance)


if __name__ == "__main__":
    same_count = 0
    N_ITER = 100000

    for _ in tqdm(range(N_ITER), desc="Simulating"):
        blue = coord()
        red = coord()
        (distance_blue, nearest_side_blue) = nearest_side(blue)

        # find the point on the side of the square which equistant
        # between blue and red