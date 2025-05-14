
def merge(left, right):
    result = [] 
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr 
    
    mid = len(arr) // 2
    left_merge = merge_sort(arr[:mid])
    right_merge = merge_sort(arr[mid:])

    return merge(left_merge, right_merge)

arr = [6,3,9,5,2,8]
arr = merge_sort(arr)
print(arr)
    
"""
arr = [6, 3, 9, 5, 2, 8]
left, right = [6,3,9], [5,2,8]

result = []
i = j = 0

(i==0) < (len(left) == 3) and (j==0) < (len(right) == 3) 
    left[i] == 6, right[j] == 5 -> left[i] >= right[j]
        result.append(right[j]) --> result = [5]
        j++

    ## j == 1 < len(right) = 3 -->
    left[i] == 6, right[j] == 2 --> left[i] >= right[j]
        result.append(right[j]) --> result = [5,2]
        j++

    ## j == 2 < len(right) = 3 
    left[i] == 6, right[j] == 8 --> left[i] <= right[j]
        result.append(left[i]) --> result = [5,2,6]
        i++

    ## i == 1 < len(left) = 3 and j == 2 < len(right) = 3 
    left[i] == 3, right[j] == 8 --> left[i] <= right[j]:
        result.append(left[i]) --> result = [5,2,6,3]
        i++

    ## i == 2 < len(left) = 3 and j == 2 < len(right) = 3 
    left[i] == 9, right[j] == 8 --> left[i] >= right[j]:
        result.append(right[j]) --> result = [5,2,6,3,8]
        j++

    ## j == 3 < len(left) == False:
        break
        
result.extend(left[i:]) --> result = [5,2,6,3,8,9]
result.extend(right[j:]) --> result = [5,2,6,3,8,9]
"""