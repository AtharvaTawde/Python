#Given an int n, print the absolute difference between n and 21, 
# except print double the absolute difference if n is over 21.
#
#
#diff21(19) → 2
#diff21(10) → 11
#diff21(21) → 0

def diff21(n):
  if n > 21:
    print(abs(n - 21) * 2)
  else:
    print(abs(n - 21))

diff21(19) #→ 2
diff21(10) #→ 11
diff21(21) #→ 0