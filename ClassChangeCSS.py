# class jugaad 
import re
import os
import fileinput
import random
def ClassChangeCSS(contents):
    pattern = '(\s\.\w+[-]?\w+)' # regex

    filedata = contents.split('\n')
    list_of_classNames = [ # this is the list of names you would use for your classes. This list is just a randomly generated sample
        'inspection',
        'inspector',
        'king',
        'ladder',
        'menu',           
        'penalty',
        'piano',
        'potato',
        'profession',
        'professor',
        'quantity',
        'reaction',
        'requirement',    
        'salad',
        'sister',
        'supermarket']

    match = re.findall(pattern, contents)
    match = [x[1:] for x in match]

    def intersection(lst1, lst2): 
        lst3 = [value for value in lst1 if value in lst2] 
        if len(lst3) != 0:
            return lst3 
    words = []
    for kk in filedata:
        if intersection(kk.split(), match) != None:
            lss = kk.split()
            lss[lss.index(intersection(lss, match)[0])] = random.choice(list_of_classNames)
            lss = ' '.join(lss)
            words.append(lss)
        else:
            words.append(kk)
    words = '\n'.join(words)

    return words
