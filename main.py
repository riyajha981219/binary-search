"""
Binary Search Algorithms

Given a list and a value; search for the value by splitting it from the middle
Note: List must be sorted.
"""

# function to search


def binarySearch(beg, end, List, key):

    # if end of the list is reached and the item isn't found
    if beg == end:
        return "Not found!"

    # if end isn't reached, find the middle of the list
    mid = beg+(end-beg)//2

    # if value is less than the item in the middle, search from the beginning to the middle of the list
    if key < List[mid]:
        return binarySearch(beg, mid, List, key)

    # if value is bigger than the item in the middle, search from the middle to the end of the list
    elif key > List[mid]:
        return binarySearch(mid+1, end, List, key)

    # if value is equal to the item in the middle, return middle position
    else:
        return mid


ogList = [67, 12, 1, 5, 2, 0, 87, 90, 105, 45, 76]
ogList = sorted(ogList)
print(f"Your original List: {ogList}")
beg = 0
end = len(ogList)
val = int(input("Search value: "))
print(f"The position is {binarySearch(beg,end,ogList,val)}")
