# merge will merge sorted lists in sorted order
# divide and conquer method and also recursive function call to merge function from merge sort 

def merge(list1, list2):
    list3 = []
    i = 0
    j=0
    while i<len(list1) and j<len(list2):
        if list1[i] < list2[j]:
            list3.append(list1[i])
            i+=1
        else:
            list3.append(list2[j])
            j+=1
    while i<len(list1):
        list3.append(list1[i])
        i += 1
    while j<len(list2):
        list3.append(list2[j])
        j += 1
    return list3

def merge_sort(mylist):
    if len(mylist) == 1:
        return mylist
    mid = int(len(mylist)/2)
    left = mylist[:mid]
    right= mylist[mid:]
    return merge(merge_sort(left), merge_sort(right))
    
print(merge_sort([13,5,6,2,1,4,7,8,19]*1000))
