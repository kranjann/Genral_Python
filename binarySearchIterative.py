# write a binary search function on a sorted array

def iterativeBinarySearch(arr, l, r, x):
    while l <= r:
         mid = l + (r-l) // 2
         if arr[mid] == x:
             return mid
         elif arr[mid] < x :
             l = mid + 1
         else:
             r = mid-1
    return -1


given_set = [4,6,8,21,43,54,65]
search = int(input("Enter the no. to be searched :"))
result = iterativeBinarySearch(given_set, 0, len(given_set)-1, search)

if result == -1:
    print("Element not found in the list")
else :
    print("Element found at :", result)