# bubble sort

list1 = [4,7,5,3,2,9]
for i in range(len(list1)-1,0,-1):
    for j in range(i):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]

print(list1)
