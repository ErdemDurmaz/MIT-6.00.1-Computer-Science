def gcdrecur(a,b):
    if b == 0:
        print("Answer is ",a)
        quit()
    else:
        gcdrecur(b,a%b)
        print(b)
gcdrecur(17,12)


