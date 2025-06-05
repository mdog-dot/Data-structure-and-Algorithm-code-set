# 希尔排序是基于插入排序的简单改进，通过预处理数组增加局部有序性，突破插入排序O(n^2)的时间复杂度
# 希尔排序的基本思路是，将数组的数按间隔h进行分组，间隔h的为一组，每组内部进行插入排序得到h有序数组
# 而后h=h/2，再将其排成h有序数组，逐步进行，直到h=1，此时再进行插入排序时，可以通过计算逆序数证明
# 数组的有序性比起最初大大增加，于是此时插入排序的时间复杂度能够突破O(N^2)
def shell_sort(nums):
    n = len(nums)
    gap = 1
    # 构造的gap的递增函数为2^(k-1);当然也可以选择其他的递增函数比如3^(k-1)
    while gap < n/2:
        gap = 2 * gap
    while gap >= 1:
        sortIndex = gap # 这里sortIndex表示第一个待排序的元素
        while sortIndex < n:
            i = sortIndex
            # 对组内元素进行插入排序，但注意这里不是以组为顺序进行的，而是按nums里元素的顺序进行的
            while i >= gap:
                if nums[i-gap] > nums[i]:
                    nums[i-gap],nums[i]=nums[i],nums[i-gap]
                else:
                    break
                i -= gap
            sortIndex += 1
        gap = gap//2
    return nums
print(shell_sort([6,4,1,3,5,4]))
                

    
