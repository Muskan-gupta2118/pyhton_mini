#second largest numer in list
def second_largest(lst):
    unique = list(set(lst))   # remove duplicates
    unique.sort()
    return unique[-2]

print(second_largest([10, 20, 30, 40, 50]))