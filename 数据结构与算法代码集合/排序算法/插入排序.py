# 冒泡排序是在选择排序的基础上，从[sortIndex:]中找出最小的元素放到sortIndex位置
# 运用逆向思维，我们还可以把sortIndex位置处的元素插入到已经排好的[:sortIndex-1]数组的正确位置
# 这就是插入排序，有点像打扑克牌把新拿到的牌插入到手里已经排好序的牌中
# 插入排序的特点是初始有序度越高，效率越高
def insert_sort(nums):
    sortIndex = 0
    while sortIndex != len(nums):
        for i in range(sortIndex, 0, -1):
            if nums[i] < nums[i-1]:
                nums[i],nums[i-1]=nums[i-1],nums[i]
            else:
                break
        sortIndex += 1
    return nums
print(insert_sort([6,4,1,3,5,4]))