# TO-DO: Complete the selection_sort() function below 
testArr = [3,5,8,2,9,0,4,6,1,7]

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # next_index = cur_index + 1
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # print(f'{arr[cur_index]}, {arr[next_index]}')
        for j in range(cur_index + 1, len(arr)):
            next_index = j
            if (arr[smallest_index] > arr[next_index]):  #Switch check for
                print(f'{arr[smallest_index]} greater than, next {arr[next_index]}')
                smallest_index = next_index
                # print(f'smallest index {smallest_index} now set to current')
        # TO-DO: swap
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp
    return arr

# selection_sort(testArr)
# print(f'\n{testArr}')

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    for i in range(0, len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                print(f'{arr[j]} > {arr[j + 1]}')
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr

bubble_sort(testArr)
print(f'\n{testArr}')

def bubble_sort2( arr ):
    # Make a flag to show if swaps have occured
    swaps_occured = True
    # Run until you get through a loop without any swaps
    while swaps_occured:
        swaps_occured = False
        # For each element in the array...
        for i in range(len(arr) - 1):
            print(arr)
            # Check it's neighbor to the right...
            if arr[i] > arr[i+1]:
                # If neighbor is smaller, swap and make Flag true
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps_occured = True

# def bubble_sort2(arr):
#     swaps_occured = True
#     while swaps_occured:
#         swaps_occured: False
#         for i in range(len(arr) - 1):
#             if arr[i] > arr[i+1]:
#                 arr[i], arr[i+1] = arr[i+1], arr[i]
#                 swaps_occured = True

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
#Time complexity: O(n^2)
#Space complexity: O(1)
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         temp = arr[1]
#         j = i
#         while (j > 0 and temp < arr[j - 1]):
#             arr[j] = arr[j -1]
#             j -= 1
#         arr[j] = temp
#     return arr
