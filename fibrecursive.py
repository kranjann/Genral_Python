# implement recursive approach for fibonacci series

def recFib(n):
    if n < 0 :
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2 :
        return 1
    else:
        return recFib(n-1) + recFib(n-2)

nterm = int(input("Enter the nterm :"))
print(recFib(nterm))