def merge_sort(arr):
    if len(arr) <= 1:
        return arr
   
    mid = len(arr) // 2
    lh = merge_sort(arr[:mid])
    rh= merge_sort(arr[mid:])

 
    return merge(lh,rh)

def merge(left, right):
    sorted_list = []
    left_idx, right_idx= 0, 0

   
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            sorted_list.append(left[left_idx])
            left_idx += 1
        else:
            sorted_list.append(right[right_idx])
            right_idx += 1

   
    sorted_list.extend(left[left_idx:])
    sorted_list.extend(right[right_idx:])

    return sorted_list

if __name__ == "__main__":
    ul= [10,2,6,7,12,22]
    print("Unsorted list:", ul)
    sl= merge_sort(ul)
    print("Sorted list:", sl)
