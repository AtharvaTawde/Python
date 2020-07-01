#Given an array of ints, return the number of 9's in the array.
#
#
#array_count9([1, 2, 9]) → 1
#array_count9([1, 9, 9]) → 2
#array_count9([1, 9, 9, 3, 9]) → 3

def array_count9(nums):
    i = 0
    for number in nums:
        if number == 9:
            i += 1
    print(i)

array_count9([1, 2, 9]) #→ 1
array_count9([1, 9, 9]) #→ 2
array_count9([1, 9, 9, 3, 9]) #→ 3