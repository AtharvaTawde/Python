#Given 2 ints, a and b, print True if one if them is 10 or if their sum is 10.
#
#
#makes10(9, 10) → True
#makes10(9, 9) → False
#makes10(1, 9) → True

def makes10(a, b):
  if (a == 10) or (b == 10) or (a + b == 10):
    print(True)
  else:
    print(False)

makes10(9, 10) #→ True
makes10(9, 9) #→ False
makes10(1, 9) #→ True