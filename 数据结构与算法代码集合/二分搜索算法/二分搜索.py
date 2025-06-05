# 基本的二分搜索：有序数组寻找一个数
def search(nums, target):
    left = 0
    right = len(nums) - 1
    # while循环里的结束条件需要根据定义的right值做出相应的调整
    # 这里定义right=len(nums)-1，说明搜索区间是[left,right]的左闭右闭区间
    # 因此循环终止条件即搜索区间内没有数存在，即left=right+1
    # 假如设置right=len(nums)，则搜索区间是[left,right)左闭右开区间，终止条件应为left=right
    while left <= right:
        # 这里mid设置与（right+left）//2等价，只是为了防止right+left太大溢出
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1

# 寻找左侧边界的二分搜索
def left_bound(nums,target):
    left = 0
    right = len(nums)
    # 这里设置为左开右闭区间
    while left < right:
        mid = left + (right-left) // 2
        if nums[mid] == target:
            # 关键！由于最后终止条件为left=right，因此这样设置不会漏掉target且能保证始终在左侧
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    # 思考：如果target不存在left会在什么位置
    # mid会把left和right都向着target附近拉，但当mid在target左边一格时，会把left拉到target右边一格
    # mid在target右边一格时会把right拉到target右边一格，因此最终left和right重合的位置一定在比target大的最小的数的位置
    if left < 0 or left >= len(nums):
        return -1
    if nums[left] == target:
        return left
    else:
        return -1

# 寻找左侧边界的二分搜索（设置左闭右闭区间的版本）
def left_bound_close(nums,target):
    left = 0
    right = len(nums) - 1
    # 设置为左闭右闭区间
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    # 因为终止条件是left = right + 1，因此可能存在索引越界的情况
    if left < 0 or left >= len(nums):
        return -1
    if nums[left] == target:
        return left
    else:
        return -1

# 寻找右侧边界的二分搜索
def right_bound(nums,target):
    left,right = 0,len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            # 这边必须得让left=mid+1，因为mid的计算总是靠向left一边，因此当right=left+1且nums[left]=target时
            # 如果取left = mid，mid会和left重合，于是left会不停地刷新在相同的位置，陷入死循环
            # 而如果取left=mid+1，最终nums[left]>target，因此right会刷新到left上达成终止条件
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    # 思考：target不存在时会返回什么
    # 最终left的位置应该和left_bound相同，但返回的是left-1，应该对应于小于target的最大的数的位置
    if nums[left - 1] == target:
        return left - 1
    else:
        return -1

# 寻找右侧边界的二分搜索（左闭右闭区间版本）
def right_bound_close(nums,target):
    left,right = 0,len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    if right < 0 or right >= len(nums):
        return -1
    if nums[right] == target:
        return right
    else:
        return -1
