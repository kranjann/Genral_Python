# write a recursive binary search function for sorted array

def searchRecursiveBinary(arr, l, r, x):
    if r >= l:
        mid = l + (r-l) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return searchRecursiveBinary(arr, l, mid-1, x)
        else :
            return searchRecursiveBinary(arr, mid+1, r, x)
    else:
        return -1


arr = [4,5,9,23,45,56,78]
search = int(input("Enter the number to be searched: "))

result = searchRecursiveBinary(arr, 0, len(arr)-1, search)

if result != -1:
    print("Element found at :", result)
else :
    print("element not found in the sorted list ")