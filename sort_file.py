def bubble_sort(list1):        #
    for j in range(len(list1)-1,0,-1):
        for i in range(j):
            if list1[i]>list1[i+1]:
                list1[i],list1[i+1]=list1[i+1],list1[i]
    return list1

def select_sort(list2):
    for i in range(len(list2)-1):
        min_index=i
        for j in range(i+1,n):
            if list2[j]<list2[min_index]:
                min_index=j
        if min_index!=i:
            list2[min_index],list2[i]=list2[i],list2[min_index]
    return list2



def insert_sort(list3):
    for i in range(1,len(list3)):
        for j in range(i,0,-1):
            if list3[j]<list3[j-1]:
                list3[j],list3[j-1]=list3[j-1],list3[j]
    return list3



def quick_sort(list4 ,start,end):
    if start>end:
        return
    mid=list4[start]
    low =start
    hign=end
    while low<hign:
        while low<hign and list4[hign]>mid:
            hign-=1
        list4[low]=list4[hign]
    list4[low]=mid
    quick_sort(list4,start,low-1)
    quick_sort(list4,low+1,end)
    return list4

def shell_sort(list5):
    n=len(list5)
    gap=n/2
    while gap>0:
        for i in range(gap,n):
            j=i
            while j>=gap and list5[j-gap]>list5[j]:
                list5[j-gap],list5[j]=list5[j],list5[j-gap]
                j-=gap
        gap=gap/2