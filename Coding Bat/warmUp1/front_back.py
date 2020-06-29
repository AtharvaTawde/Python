#Given a string, return a new string where the first and last chars have been exchanged.
#
#
#front_back('code') → 'eodc'
#front_back('a') → 'a'
#front_back('ab') → 'ba'

def front_back(str):
  if len(str) >= 1:  
    str = list(str)
    x = str[0]
    y = str[-1]
    str[-1] = x
    str[0] = y
    print(''.join(str))
  else:
    print(str)

front_back('code') #→ 'eodc'
front_back('a') #→ 'a'
front_back('ab') #→ 'ba'