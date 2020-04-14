# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


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
