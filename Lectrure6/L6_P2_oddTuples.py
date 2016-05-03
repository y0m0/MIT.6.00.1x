def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    newtup = ()
    for i in aTup[::2]:
            newtup += (i,)
    return newtup
