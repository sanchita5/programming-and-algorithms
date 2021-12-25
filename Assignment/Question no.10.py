#Python program to iteration over sets.
set1={1,2,3,4,5,8,9,10}
for i in set1:
    print(i,end=" ")
print()
l1=list(set1)
for j in range(len(set1)):
    print(l1[j],end=" ")
