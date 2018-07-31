def get_neighbourhood(n_type, arr, coordinates):
    print(arr)
    print(len(arr))
    i, j = coordinates

    if not arr:
        return []

    for x in arr:
        if i > len(x) or j > len(x):
            return []
        if len(x) == 0:
            return []

    print(coordinates)

    if n_type == 'moore':
        moore = []
        if i - 1 < 0 and j - 1 < 0:
            moore = [arr[i][j + 1], arr[i + 1][j], arr[i + 1][j + 1]]
            return moore

#         if i - 1 < 0:
            moore = [arr[i][j - 1], arr[i][j + 1], arr[i + 1]
                     [j - 1], arr[i + 1][j], arr[i + 1][j + 1]]
            return(moore)

        if j - 1 < 0:
            moore = [arr[i][j + 1], arr[i - 1][j], arr[i - 1]
                     [j + 1], arr[i + 1][j], arr[i + 1][j + 1]]
            return(moore)

        if i + 1 >= len(arr) and j + 1 < len(arr):
            moore = [arr[i][j - 1], arr[i][j + 1], arr[i - 1]
                     [j - 1], arr[i - 1][j], arr[i - 1][j + 1]]
            return(moore)

        if j + 1 >= len(arr) and i + 1 < len(arr):
            moore = [arr[i][j - 1], arr[i - 1][j - 1],
                     arr[i - 1][j], arr[i + 1][j - 1], arr[i + 1][j]]
            return(moore)

        if 0 < i < len(arr) - 1 and 0 < j < len(arr) - 1:
            moore = [arr[i][j - 1], arr[i][j + 1], arr[i - 1][j - 1], arr[i - 1][j],
                     arr[i - 1][j + 1], arr[i + 1][j - 1], arr[i + 1][j], arr[i + 1][j + 1]]
            return(moore)

    if n_type == 'von_neumann':
        if i - 1 < 0 and j - 1 < 0:
            von = [arr[i][j + 1], arr[i + 1][j]]
            return von
        if i - 1 < 0:
            von = [arr[i][j + 1], arr[i][j - 1], arr[i + 1][j]]
            return von
        if j - 1 < 0:
            von = [arr[i][j + 1], arr[i - 1][j], arr[i + 1][j]]
            return von
        if i + 1 >= len(arr):
            von = [arr[i][j + 1], arr[i][j - 1], arr[i - 1][j]]
            return von

        if j + 1 >= len(arr):
            von = [arr[i][j - 1], arr[i - 1][j], arr[i + 1][j]]
            return von
        else:
            von = [arr[i][j + 1], arr[i][j - 1], arr[i - 1][j], arr[i + 1][j]]
        return(von)


arr = [[-3, 1, -9, -3, 10, 5, -9, -8, -5, -7, -3, 2], [8, -3, 9, 2, 9, -3, -3, 10, 5, -4, 8, -7], [-10, 3, -10, -7, 3, -10, -7, -8, 3, 4, 8, -8], [1, -6, -7, -10,
                                                                                                                                                   2, 5, -10, -3, -6, 0, -10, -2], [-4, 2, -2, -5, -1, 9, 3, -5, -7, 6, -9, -4], [-7, -1, 2, -5, 0, 10, 1, -7, -2, 6, -5, 9], [-1, 0, 8, 6, -9, 6, 2, -1, 0, 6, 6, 8]]

indexes1 = (3, 10)
print('Moore', get_neighbourhood('moore', arr, indexes1))
print('Von', get_neighbourhood('von_neumann', arr, indexes1))
