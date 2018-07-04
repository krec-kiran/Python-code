class BinFind:
    def __init__(self,array,upper):
        self.upper = upper
        self.array = array

    def find(self,num):
        lower = 0
        upper = self.upper
        while lower <= upper:
            mid = (int((lower + upper) / 2))
            if (num < array[mid]):
                upper = mid - 1
            if (num > array[mid]):
                lower = mid + 1
            elif ( num == array[mid] ):
                return mid
        return -1

if __name__ == "__main__":
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    t=BinFind(array, len(array) - 1)
    x = t.find(2)

    if x == -1:
        print("Not Found")
    else:
        print("found")
