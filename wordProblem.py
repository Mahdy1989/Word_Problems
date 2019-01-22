# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:18:45 2019

@author: pc-name MSUS
"""
# patterns to look for
pats = ('a','e','u','o','y','i')

target_length = len(pats)

sentence = '''What is this problem? Is it impossible that these letters 
            "couuuuue(?)ld/" all take place together" in a "word." or can you
            guess a word that does and it is the shortest?"///'''

# selection criteria
# 1. different kinds and maximum number of letters identified in pats
ndf = 0 # number of different kinds where each kind is counted once only
# 2. shortest word

words = enumerate(sentence.split(' '))

######
'''All words dictionary --> word:word_length, [patterns], number_of_patterns'''
d = {}
######


def MakeAlphabetic(word_phrase):
    '''This function ensures non_chars do not exist in word_phrase'''
    non_chars = {'.':None, ',':None, "'":None,'"':None, '?':None, '!':None, 
                 "-":None, '_':None, "&":None, "$":None, "/":None, "\\":None, 
                 "@":None, "#":None, "%":None, "*":None, "(":None, ")":None, 
                 "[":None, "]":None, "+":None, "^":None, "~":None, "<":None, 
                 ">":None, "|":None, '\n':None, ':':None, ';':None}
    z = [item for item in word_phrase if item not in non_chars]
    return "".join(z) # converting all list items back to text
    
             
for word in words:
    w = word[1]
    if w.isalpha():
        # k_prime is a list of pats 
        k_prime = [pat for pat in pats if pat in w]
        d[w] = [len(w), set(k_prime), len(set(k_prime))]
    else:
        w = MakeAlphabetic(w)
        # k_prime is a list of pats 
        k_prime = [pat for pat in pats if pat in w]
        d[w] = [len(w), set(k_prime), len(set(k_prime))]

del word, w, k_prime
  
answer = []
c = 0 # counter meant to count the very first iteration
ndf_old = 0

for k, v in d.items():
    ndf = v[2]
    if c == 0: # initialization
        ndf_old = ndf
        c += 1
        answer.append([k, v[0], v[1], ndf])
    ############################################
    else:
        if ndf_old < ndf:
            answer.clear()
            answer.append([k, v[0], v[1], ndf]) # choose the new answer
            ndf_old = ndf
        ############################################
        elif ndf_old > ndf:
            pass # keep the old answer
        ############################################
        else:
            if answer[0][1] > len(k): # len(k_old) > len(k_new)
                answer.clear()
                answer.append([k, v[0], v[1], ndf]) # choose the new answer
            ############################################
            elif answer[0][1] < len(k): # len(k_old) < len(k_new)
                pass # keep the old answer
            ############################################
            else:
                answer.append([k, v[0], v[1], ndf]) # adding another answer
        
print(answer[0][0],"is the shortest word in the text which has most of the patterns")
print("Details:\t",answer[0])
