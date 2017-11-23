class BinSearch:
    def __init__(self, array, upper):
        self.upper = upper
        self.array = array

    def search(self, n):
        lower = 0
        upper = self.upper
        while lower <= upper:
            mid = (int((lower + upper) / 2))
            if(n < array[mid]):
                upper = mid - 1
            if(n > array[mid]):
                lower = mid + 1
            elif(n == array[mid]):
                return mid
        return -1

if __name__ == "__main__":
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    t = BinSearch(array, len(array) - 1)
    x = t.search(3)

    if x == -1:
        print("not found")
    else:
        print("found")
