# xs = [100, 76, 56, 44, 89, 73, 68, 56, 64,123, 2333, 144, 50, 132, 123, 34, 89]

ls = [50, 55, 57, 58, 60]
#
# [50, 55, 57], [50, 55, 58], [50, 55, 60], [50, 57, 58], [50, 57, 60], [
#     50, 58, 60], [55, 57, 58], [55, 57, 60], [55, 58, 60], [57, 58, 60]


for x in range(0, len(ls)):
    elements = ls[:x + 2]
    k = ls[:x] + ls[x + 1:]
    print(elements, k)