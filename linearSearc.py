# given a list of numbers find a specific number

def linearSearch(arr, n, x):
    for i in range(0, n):
        if x == arr[i]:
            return i
    return -1


given_set = [21, 23, 4, 5, -1]
len_of_array = len(given_set)
findTerm = int(input("Enter the term to search:"))
result = linearSearch(given_set, len_of_array, findTerm)

if result == -1:
    print("Number not found in the list.")
else :
    print("Number is found at: ", result)

