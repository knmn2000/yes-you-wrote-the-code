# class jugaad 
import re
import os
import fileinput
import random
def classJugaad(contents):
    #code = open('D:\prog\github_ka_maal\yes-you-wrote-the-code-master\code.txt', 'r')
    #contents = code.read()
    pattern = '(\s\.\w+[-]?\w+)'



    #with open('D:\prog\github_ka_maal\yes-you-wrote-the-code-master\code.txt', 'r') as file:
     #   filedata = file.read().split('\n')
    #file.close()
    filedata = contents.split('\n')
    list_of_classNames = ['ek','do','3','insect',
        'inspection',
        'inspector',
        'king',
        'ladder',
        'menu',            # Copied a random word ki list from here and there
        'penalty',
        'piano',
        'potato',
        'profession',
        'professor',
        'quantity',
        'reaction',
        'requirement',     # make a list of class names that you would probab use
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

    # magicc af 
    print('blllaaa')
    return words

    '''with open('iWroteTheGoddamnCodeFFS.txt', 'w') as rektSimulator3000:
        rektSimulator3000.write(words)'''