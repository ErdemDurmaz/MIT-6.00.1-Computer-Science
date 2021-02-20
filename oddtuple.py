def oddTuples(aTup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup.
    '''
    for i, item in enumerate(aTup):
        if (i) % 2 == 0:
            print(item, end = " ")
oddTuples(('I', 'am', 'a', 'test', 'tuple'))