#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
#
#
#array123([1, 1, 2, 3, 1]) → True
#array123([1, 1, 2, 4, 1]) → False
#array123([1, 1, 2, 1, 2, 3]) → True

def array123(nums):
    match = [1, 2, 3]
    lst = []
    for s in range(len(nums)):
        lst.append(nums[s:s+3])

    if match in lst:
        print(True)
    else:
        print(False)

array123([1, 1, 2, 3, 1]) #→ True
array123([1, 1, 2, 4, 1]) #→ False
array123([1, 1, 2, 1, 2, 3]) #→ True