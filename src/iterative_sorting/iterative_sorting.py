# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        next_index = cur_index + 1
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        print(f'{arr[cur_index]}, {arr[next_index]}')
        if (arr[smallest_index] < arr[next_index]):
            print(f'{arr[smallest_index]} less than, next {arr[next_index]}')
            smallest_index = cur_index
            print(f'smallest index {smallest_index} now set to current')




        # TO-DO: swap




    return arr

selection_sort([3,5,8,2,9,0,4,6,1,7])

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         temp = arr[1]
#         j = i
#         while (j > 0 and temp < arr[j - 1]):
#             arr[j] = arr[j -1]
#             j -= 1
#         arr[j] = temp
#     return arr
