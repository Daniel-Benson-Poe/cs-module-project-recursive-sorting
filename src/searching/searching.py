# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # check if start greater than end
    if start > end:
        # return none
        return -1
    else:
        # set midpoint of array
        midpoint = (start + end) // 2
        # check if midpoint and target are equal
        if arr[midpoint] == target:
            return midpoint
        # check if midpoint value is less than target        
        elif arr[midpoint] < target:
            # recursively run binary search again setting start to midpoint + 1
            return binary_search(arr, target, midpoint + 1, end)
        else:
            # recursively run binary search again setting end to midpoint - 1
            return binary_search(arr, target, start, midpoint - 1)

            
# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
