testArr = [3,5,8,2,9,0,4,6,1,7]

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    arrC = []
    # print(arrC)
    while (len(arrA) > 0 and len(arrB) > 0):
        if arrA[0] > arrB[0]:
            arrC.append(arrB[0])
            arrB.pop(0)
        else:
            arrC.append(arrA[0])
            arrA.pop(0)
    while (len(arrA) > 0):
        arrC.append(arrA[0])
        arrA.pop(0)
    while (len(arrB) > 0):
        arrC.append(arrB[0])
        arrB.pop(0)
    
    return arrC


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # print(arr)
    if (len(arr) == 1):
        return arr
    mid_index = len(arr) // 2
    # print(f'Mid index: {mid_index}')
    arr1 = arr[mid_index:]
    arr2 = arr[:mid_index]

    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)

    return merge(arr1, arr2)

# merge_sort(testArr)
print(merge_sort(testArr))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


#########################################
def factorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

def factorial(n):
    if n <= 1: #base case
        return 1 
    return n * factorial(n-1)

#######################################
def quicksort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[0]
    smaller = []
    larger = []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            smaller.append(arr[i])
        else:
            larger.append(arr[i])
    # smaller = quicksort(smaller)
    # larger = quicksort(larger)
    return quicksort(smaller) + [pivot] + quicksort(larger)

# MERGESORT
# [2, 0, 1, 3, 6, 9, 8, 5, 7, 4]
# ​
# # (base case) If the array is empty or length 1, return
# ​
# # Split the arrays into half
# arr1 = [2, 0, 1, 3, 6]
# arr2 = [9, 8, 5, 7, 4]
# ​
# # Sort each half
# arr1 = [0,1,2,3,6]
# arr2 = [4,5,7,8,9]
# ​
# # Merge them back together
# # Compare the first values of each array, add smaller of the 2 to result
# merged = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
