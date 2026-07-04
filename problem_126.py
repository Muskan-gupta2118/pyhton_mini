#move all the zero till the end
def move_zero(arr):

    result = []

    count = 0

    for num in arr:
        if num != 0:
            result.append(num)
        else:
            count += 1

    result.extend([0]*count)

    return result

print(move_zero([1,0,3,0,5,0]))