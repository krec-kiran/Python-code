import re
import apath
import numpy
import path_file_open


def getInputFile():
    mp = path_file_open.extractInput()
    k = mp.split(',')
    return k


def getGoal(k):
    route = []
    route.append(k[0])
    route.append(k[-1])

    path = []
    for x in route:
        p = re.findall(r'\d+', x)
        path.append((tuple(int(x) for x in p)))
    return path


def getCoordinates(k):
    val = []
    for x in k:
        p = re.findall(r'\d+', x)
        val.append((tuple(int(x) for x in p)))
    return val

# create grid now


def createGrid(val):
    grid_max_x = max(val, key=lambda item: item[0])
    grid_max_y = max(val, key=lambda item: item[1])

    print(grid_max_x, grid_max_y)

    grid_min = min(val, key=lambda item: item[1])
    grid_max = max(val, key=lambda item: item[1])

    grid = []
    for x in range(0, grid_max_x[0] + 1):
        for y in range(0, grid_max_y[1] + 1):
            grid.append((y, x))
    print(grid, grid_max[1], grid_max[0])
    return grid, grid_max_x


def createMap():
    result_map = []
    my_map = []
    k = getInputFile()
    path = getGoal(k)
    orginal = getCoordinates(k)
    grid, grid_max = createGrid(orginal)
    for x in grid:
        if x in orginal and x not in path:
            my_map.append('1')
            result_map.append('x')
        else:
            if x == path[0]:
                result_map.append('S')
                my_map.append('0')
            elif x == path[1]:
                result_map.append('E')
                my_map.append('0')
            else:
                my_map.append('0')
                result_map.append('.')
    final = createMatrix(my_map, grid_max)
    print('Path', final)
    g = sorted(grid,  key=lambda x: x[0])

    # code to output as in expected legend - todo tomorrow
    legend = []

    for i in range(len(g)):
        i = '.'
    for i in grid:
        if i in final[1:]:
            legend.append('O')
        if i == path[0]:
            legend.append('S')
        elif i == path[1]:
            legend.append('E')
        elif i in orginal and i not in final[1:]:
            legend.append('x')
        elif i not in orginal and i not in final[1:]:
            legend.append('.')

    print('Legend', legend)


def createMatrix(my_map, grid_max_x):
    result = []
    start = 0
    end = 0
    for i in range(int(len(my_map) / (grid_max_x[0] + 1))):
        end += grid_max_x[0] + 1
        result.append([int(x) for x in my_map[start:end]])
        start = end
    nmap = numpy.array(result)
    data = apath.astar(nmap, (1, 0), (3, 0))
    data = [(t[1], t[0]) for t in data]
    return data


createMap()
