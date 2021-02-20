def oddTuples(aTup):
    '''
    Write a procedure called oddTuples, which takes a tuple as input,
    and returns a new tuple as output, where every other element of the input tuple is copied,
    starting with the first one.
    aTup: a tuple
    returns: tuple, every other element of aTup.
    '''
    myarray = []
    
    
    
    
    for i, item in enumerate(aTup):
        if (i) % 2 == 0:
            myarray.append(item)

    return tuple(myarray)    

print(oddTuples(("a","b","c","d","e","f")))
