def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        # 类似合并链表来进行操作
        p1,p2,p = 0,0,0
        while p1 != len(lefthalf) and p2 != len(righthalf):
            if lefthalf[p1] < righthalf[p2]:
                alist[p] = lefthalf[p1]
                p1 += 1
            else:
                alist[p] = righthalf[p2]
                p2 += 1
            p += 1
        # 剩余元素直接接在alist的指针p后面
        if p1 < len(lefthalf):
            while p1 != len(lefthalf):
                alist[p] = lefthalf[p1]
                p += 1
                p1 += 1
        if p2 < len(righthalf):
            while p2 != len(righthalf):
                alist[p] = righthalf[p2]
                p += 1
                p2 += 1
alist = [1,3,4,2,9,7,5]
mergeSort(alist)
print(alist)