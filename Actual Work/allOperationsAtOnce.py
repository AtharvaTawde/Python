print 'Welcome to the All Operator! This unique calculator does all possible operations on two numerical values at once!'
print 'So no need to type those pesky multiplication signs and whatnot!'

while True:
    one = raw_input('First number: ')
    two = raw_input('Second number: ')

    try:
        one = float(one)
        two = float(two)
        print one, '+', two, '=', str(one + two)
        print one, '-', two, '=', str(one - two)
        print one, 'x', two, '=', str(one * two)
        print one, '/', two, '=', str(one / two)
        print str(one) + '^' + str(two), '=', str(one ** two)
    except:
        print 'Type in numerical values, bud!'

    print '------------------------------------------------\n'