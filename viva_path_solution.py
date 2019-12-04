import re
import apath
import numpy
import sys
import path_file_open


def getInputFile():
    if len(sys.argv) < 2:
        print(
            'Please supply input file of format - path-[*].txt - to run the script')
        exit(0)
    elif len(sys.argv) == 2:
        lines = path_file_open.extractInput(sys.argv[1])
        coordinates = lines.split(',')
        return coordinates


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

# create Grid now


def createGrid(val):
    grid_min = min(val, key=lambda item: item[1])
    grid_max = max(val, key=lambda item: item[1])
    grid = []
    for x in range(0, grid_max[1] + 1):
        for y in range(0, grid_max[0] + 1):
            grid.append((y, x))
    return grid, grid_max


def createMap():
    route_map = []
    astar_map = []
    input_file = getInputFile()
    path = getGoal(input_file)
    goal_coordinates = getCoordinates(input_file)
    grid, grid_max = createGrid(goal_coordinates)
    for x in grid:
        if x in goal_coordinates and x not in path:
            astar_map.append('1')
            route_map.append('x')
        else:
            if x == path[0]:
                route_map.append('S')
                astar_map.append('0')
            elif x == path[1]:
                route_map.append('E')
                astar_map.append('0')
            else:
                astar_map.append('0')
                route_map.append('.')

    optimal_path = findPath(astar_map, grid_max)
    createLegend(grid, optimal_path, path, goal_coordinates)


def findPath(astar_map, grid_max):
    result = []
    start = 0
    end = 0
    for i in range(int(len(astar_map) / (grid_max[0] + 1))):
        end += grid_max[0] + 1
        result.append([int(x) for x in astar_map[start:end]])
        start = end
    nmap = numpy.array(result)
    data = apath.astar(nmap, (0, 0), (2, 2))
    data = [(t[1], t[0]) for t in data]
    return data


def createLegend(grid, optimal_path, path, goal_coordinates):
    legend = []
    for i in grid:
        if i in optimal_path[1:]:
            legend.append('O')
        if i == path[0]:
            legend.append('S')
        elif i == path[1]:
            legend.append('E')
        elif i in goal_coordinates and i not in optimal_path[1:]:
            legend.append('x')
        elif i not in goal_coordinates and i not in optimal_path[1:]:
            legend.append('.')
    f = open('path-basic.txt' + '.answer', 'w')
    f.write(''.join(legend))


def main():
    createMap()


if __name__ == "__main__":
    main()
