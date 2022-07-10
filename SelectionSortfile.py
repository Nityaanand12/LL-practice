# selection sort compare and find minimum value and get exchanges with exist index


def selection_sort(mylist):
    n = len(mylist)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if mylist[min_index] > mylist[j]:
                min_index = j
        if min_index != i:
            mylist[i], mylist[min_index] = mylist[min_index], mylist[i]
    return mylist

print(selection_sort([7,6,4,8,9,2,4,5,1,3]))
