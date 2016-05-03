animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    longest = None
    for k in aDict.iterkeys():
        if longest is None or len(aDict[k]) > len(aDict[longest]) :
            longest = k
    return longest        
            
