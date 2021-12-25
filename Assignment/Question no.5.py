# Python program to print a specified list after removing the 4th elements.
list=[10,20,30,40,60]
for i in list:
    if i==list[2]:
        continue
    print(i,end=" ")