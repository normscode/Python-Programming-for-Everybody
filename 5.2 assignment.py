largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        num_b = int(num)
    except:
        print("Invalid input")
        continue
    if smallest is None:
        smallest = num_b
    elif num_b < smallest:
        smallest = num_b
    elif largest is None:
        largest = num_b
    elif num_b > largest:
        largest = num_b

print("Maximum is", largest)
print("Minimum is", smallest) 