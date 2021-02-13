'''
Write an iterative function, gcdIter(a, b),
that implements this idea. One easy way to do this is to begin with a test value equal
to the smaller of the two input arguments, and iteratively reduce this test value by 1
until you either reach a case where the test divides both a and b without remainder, or you reach 1.
'''
def gcditer(a,b):
    if a > b :
        for i in range(6,0):
            if a % b == 0:
                print("Found it a")
        b -=1
    if b > a :
        for i in a :
            if b % a == 0:
                print("Found it b")
            a -=1
gcditer(12,6)