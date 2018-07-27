import math


def furthestDistance(arr):
    print(arr)
    if len(arr) == 2:
        x_distance = pow((arr[0][0] - arr[1][0]), 2)
        y_distance = pow((arr[0][1] - arr[1][1]), 2)
        distance = x_distance + y_distance
        distance = math.sqrt(distance)
        distance = round(distance, 2)
        return(distance)
    else:
        l = [x for x, y in arr]
        max_x = min(l)
        index_1 = l.index(max_x)
        point_a = arr[index_1]

        m = [y for x, y in arr]
        max_y = max(m)
        index_2 = m.index(max_y)
        point_b = arr[index_2]

        k = list(zip(point_a, point_b))

        distance = [(x - y) * (x - y) for x, y in k]
        distance = distance[0] + distance[1]

        distance = math.sqrt(distance)
        distance = round(distance, 2)
        print(distance)
        return(distance)
