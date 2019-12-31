import sys


def insertion_sort(unsorted_arr):
    for i in range(len(unsorted_arr)):
        # take the first element as the key
        key = unsorted_arr[i]
        j = i
        # place the key in the sorted sequence on the left hand side
        while j > 0 and unsorted_arr[j - 1] >= key:
            unsorted_arr[j] = unsorted_arr[j-1]
            j -= 1
        unsorted_arr[j] = key
        #print(f"List looks like {unsorted_arr} after Iteration: {i + 1}")
    return unsorted_arr


def merge(array, start, mid, end):
    # create 2 temp sub lists to hold all the values
    temp_list1 = []
    temp_list2 = []
    for i in range(start, mid + 1):
        temp_list1.append(array[i])
    for j in range(mid + 1, end + 1):
        temp_list2.append(array[j])

    temp_list1.append(sys.maxsize)
    temp_list2.append(sys.maxsize)

    #print(f"Array: {array}, Temp List1: {temp_list1}, Temp List2: {temp_list2} , Start: {start}, End: {end}")
    i = 0
    j = 0

    for k in range(start, end + 1):
        if temp_list1[i] < temp_list2[j]:
            array[k] = temp_list1[i]
            i += 1
        else:
            array[k] = temp_list2[j]
            j += 1


def merge_sort(unsorted_arr, start, end):
    # base condition is when only one element is left in the array
    if start < end:
        # find the middle index to break the array into 2 halves
        mid_index = int((start + end)/2)

        # call merge sort on each half
        merge_sort(unsorted_arr, start, mid_index)
        merge_sort(unsorted_arr, mid_index + 1, end)

        # merge the resulting halves into a sorted array
        merge(unsorted_arr, start, mid_index, end)


def partition(array, start, end):
    # Take the last element of the array as the pivot
    pivot_el = array[end]
    i = start - 1
    for j in range(start, end):
        if array[j] <= pivot_el:
            i += 1
            temp = array[j]
            array[j] = array[i]
            array[i] = temp

    temp = array[i + 1]
    array[i + 1] = pivot_el
    array[end] = temp
    #print(f"Array after partition looks like {array}")
    return i + 1


def quick_sort(unsorted_arr, start, end):
    if start < end:
        # base condition when there is exactly one element left; return
        pivot_index = partition(unsorted_arr, start, end)
        quick_sort(unsorted_arr, start, pivot_index - 1)
        quick_sort(unsorted_arr, pivot_index + 1, end)


def bubble_sort(unsorted_arr):
    # Logic is to bubble up the highest value in the array i.e. place it at the end
    for i in range(len(unsorted_arr)):
        swapped = False
        for j in range(len(unsorted_arr) - i - 1):
            if unsorted_arr[j] > unsorted_arr[j + 1]:
                temp = unsorted_arr[j]
                unsorted_arr[j] = unsorted_arr[j + 1]
                unsorted_arr[j + 1] = temp
                swapped = True
        #print(f"After Iteration {i + 1}, Array looks like: {unsorted_arr}")
        # If we haven't swapped in the previous loop it means the array is already sorted
        if not swapped:
            break

if __name__ == '__main__':
    print("INSERTION SORT")
    unsorted_list1 = [4, 5, 3, 2, 1]
    print(f"Unsorted List: {unsorted_list1}")
    insertion_sort(unsorted_list1)
    print(f"Sorted List: {unsorted_list1}")

    print("MERGE SORT")
    unsorted_list2 = [9, 1, 3, 6, 3, 2]
    print(f"Unsorted List: {unsorted_list2}")
    merge_sort(unsorted_list2, 0, len(unsorted_list2) - 1)
    print(f"Sorted List: {unsorted_list2}")

    print("QUICK SORT")
    unsorted_list3 = [5, 4, 1, 2, 3]
    print(f"Unsorted List: {unsorted_list3}")
    quick_sort(unsorted_list3, 0 , len(unsorted_list3) - 1)
    print(f"Sorted List: {unsorted_list3}")

    print("BUBBLE SORT")
    unsorted_list4 = [5, 4, 1, 2, 3]
    print(f"Unsorted List: {unsorted_list4}")
    bubble_sort(unsorted_list4)
    print(f"Sorted List: {unsorted_list4}")