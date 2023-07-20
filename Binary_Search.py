l1 = input("Enter a list of numbers, separated by spaces: ")
l = l1.split()

print("The user input list is",l)

n = int(input("enter the number you need to find :"))

low = 0
high = len(l) - 1
mid = 0
print("High value of the list will be at index:", high)
mid = (low + high) // 2
print("Mid value is:", mid)

while low <= high:
    if int(l[mid] )< n:
        low = mid + 1
    elif int(l[mid]) > n:
        high = mid - 1
    else:
        print("The given number is found at index:", mid)
        break
    mid = (low + high) // 2

if low > high:
    print("The given number is not found in the list.")
