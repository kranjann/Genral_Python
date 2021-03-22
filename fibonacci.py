# write a function to print n fibonacci sequence

def fibonacci(ntem):
    n1 = 0
    n2 = 1
    count = 0

    if nterm < 0:
        print("Please enter positive integer.")
    elif nterm <= 1:
        print(1)
    else:
        while count < nterm :
          print(n1)
          nth = n1 + n2
          n1 = n2
          n2 = nth
          count += 1

nterm = int(input("Enter the nterm :"))
fibonacci(nterm)