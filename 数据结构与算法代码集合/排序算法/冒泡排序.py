# 选择排序是每次选出[sortIndex:]数组里最小的数和sortIndex位置的数交换，但是这步交换操作导致排序无稳定性，且当数组已经是有序时，选择排序不会终止
# 冒泡排序是对选择排序的一种改进，即让最小的数像冒泡一样从左往右一路交换到sortIndex位置，而且可以引入swap来判断一次冒泡过程中有没有发生交换
# 若没有交换，代表数组已经排好了，可以提前终止排序，其时间复杂度和选择排序一样，都是O(n)
def bubble_sort(nums):
    # sortIndex到数组末端的子数组是未排序过的
    sortIndex = 0
    while sortIndex != len(nums)-1:
        # 引入swap标记一次冒泡中是否有交换
        swap = False
        for i in range(len(nums)-1, sortIndex, -1):
            if nums[i] < nums[i-1]:
                nums[i],nums[i-1]=nums[i-1],nums[i]
                swap = True
        if swap == False:
            return nums
        sortIndex += 1
    return nums
print(bubble_sort([3,4,2,1,5]))           