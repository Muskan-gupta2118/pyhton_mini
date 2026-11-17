#linear search

def linear_search(arr,target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1

print(linear_search([2,7,6,8,5],6))