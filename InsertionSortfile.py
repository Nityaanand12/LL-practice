# picked up index to reversed order till starting index and exchange values in between
# pick from 1 check 0
# pick from 2 and checks 1, 0 index

def insertion_sort(mylist):
    n = len(mylist)
    for i in range(1, n):
        for j in range(i-1,-1,-1):
            if mylist[j]<mylist[i]:
                mylist[j], mylist[i] = mylist[i], mylist[j]
                i=j
    return mylist

def insertion_sort_otherway(mylist):
    n = len(mylist)
    for i in range(1,n):
        j = i -1
        while mylist[i] < mylist[j] and j>-1:
            mylist[j+1], mylist[j] =mylist[j], mylist[j+1]
            i=j
            j -= 1
    return mylist

print(insertion_sort_otherway([7,3,2,4,5,1,6]))
