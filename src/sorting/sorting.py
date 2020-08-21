# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB) # combine lengths of both array to get total length
    merged_arr = [] # Create empty list for our new merged array

    # Your code here
    a = 0 # set a index counter to 0
    b = 0 # set b index counter to 0

    while a < len(arrA) and b < len(arrB): # Loop as long as a < length of array A AND b < length of array B
        if arrA[a] < arrB[b]: # Set condition: if array A at index a < array B at index b
            merged_arr.append(arrA[a]) # append array A at index a into merged_arr array
            a += 1 # increment the a index counter by 1
        
        else: # If above condition not met: 
            merged_arr.append(arrB[b]) # append array B at index b into merged_arr array
            b += 1 # increment the b index counter by 1

    if a < len(arrA): # Check condition: if index counter a < length of array A
        merged_arr.extend(arrA[a:]) # extend the merged_arr array by whatever remaining elements are contained within array A

    if b < len(arrB): # Check condition: if index counter b < length of array B
        merged_arr.extend(arrB[b:]) # extend the merged_arr array by whatever remaining elements are contained within array B

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1: # Check condition: if length of array > 1 seperate array into left and right halves
        left = merge_sort(arr[0:len(arr)//2]) # create left side of array using merge_sort function above
        right = merge_sort(arr[len(arr)//2:]) # create right side of array using merge_sort function above

        arr = merge(left, right) # merge left and right into the array

    return arr
