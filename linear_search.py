list = [1,2,3,4,5]
n = int(input("Enter the number to find the nummber in the list :- "))
lenght = len(list)
for i in range(0,lenght):
    if list[i] == n:
        print("Number is Found in the list")
        break
else:
     print("not Found in the list")