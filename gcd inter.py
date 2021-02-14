'''
Write an iterative function, gcdIter(a, b),
that implements this idea. One easy way to do this is to begin with a test value equal
to the smaller of the two input arguments, and iteratively reduce this test value by 1
until you either reach a case where the test divides both a and b without remainder, or you reach 1.
'''
def gcditer(a,b):
    lowest = min(a,b)
    biggest = max(a,b)
    orglowest = lowest
    #orgbiggest = biggest
    while lowest >0:
        
        if biggest % lowest == 0 and orglowest % lowest == 0:
            print('Found it',lowest)
            quit()
        lowest -= 1
        
gcditer(17,12)