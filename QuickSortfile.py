def pivot(mylist, pivot_index, end_index):
    swap = pivot_index
    for i in range(pivot_index+1,end_index+1):
        if mylist[i] < mylist[pivot_index]:
            swap += 1
            mylist[swap], mylist[i] = mylist[i], mylist[swap]
    mylist[swap], mylist[pivot_index] = mylist[pivot_index], mylist[swap]
    return swap
    
def quick_sort_helper(mylist, left, right):
    if left < right:
        pivot_point = pivot(mylist, left, right)
        quick_sort_helper(mylist, left, pivot_point-1)
        quick_sort_helper(mylist, pivot_point+1, right)
    return mylist

def quick_sort(mylist):
    return quick_sort_helper(mylist, 0, len(mylist)-1)
    
print(quick_sort([3,6,8,1,7,8,9]))


            
            
