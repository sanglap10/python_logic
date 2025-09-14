def hello():
    names = ["bhaskar","sanglap","fuyfu","ytdy"]
    for i in names:
        print(f"hello {i}")






def even_odd():
    numbers = [9,25,2,66,99,8,1]
    even = []
    odd = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    print(f"even = {even}")
    print(f"odd = {odd}")

def largest(arr):
    largest = arr[0]
    for n in arr:
        if n > largest:
            largest = n
    print(f"{largest} is largest")

def smallest(arr):
    smallest = arr[0]
    for i in arr:
        if i < smallest:
            smallest = i
    print(f"{smallest} is smallest")



numbers = [45,8,100,65,201,505,55]
smallest(numbers)
largest(numbers)
#even_odd()
