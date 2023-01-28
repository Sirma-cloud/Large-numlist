list = []
num = int(input("Enter number of elements in list: "))
for i in range(1, num+1):
    new = int(input("Enter elements: "))
    list.append(new)
print("Largest element is:", max(list))

" or "

list1 = [5, 7, 2, 8]
print("This is the largest number: ", max(list))
