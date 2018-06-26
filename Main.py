# Scrambling-words-using-python-and-filehandling-concepts

#!/usr/bin/python
# -*- coding: utf-8 -*-

def scramble(unscrambled):
    ''' 
    Scrambles the word(s) in unscrambled such that the first and last letter remain the same,
    but the inner letters are scrambled. Preserves the punctuation.
    '''
    import string, random, re
    splitter = re.compile(r'\s')
    words = splitter.split(u''.join(ch for ch in unscrambled if ch not in set(string.punctuation)))
    for word in words:
        if len(word) < 4: continue
        mid = list(word[1:-1])
        random.shuffle(mid)
        scrambled = u'%c%s%c' % (word[0], ''.join(mid), word[-1])
        unscrambled = unscrambled.replace(word, scrambled, 1)
    f2=open("MyFileScrambled","w")
    f2.write(unscrambled)
    
    print(unscrambled)

if __name__ == '__main__':
    f1=open("MyFile","r")
    scramble(f1.read())
