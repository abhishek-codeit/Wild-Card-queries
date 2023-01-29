# Dependency Installation
# pip install gensim pandas

import pandas as pd;    
from gensim.utils import tokenize

# reading documents from files
doc1 = open("doc1.txt",'r').read()
doc2 = open("doc2.txt",'r').read()

# tokenizing the documents
tok_1 = list(tokenize(doc1))
tok_2 = list(tokenize(doc2))

dic = dict()

# creating a dictionary with documents id as values
for i in tok_1:
    dic[i] = 1
    
for i in tok_2:
    dic[i] = 2

# creaating permuterm index by appending $ to the start and end of each word
permuterms = {}
keys = {}
kgram = 2
for k,v in dic.items():
    val = '$'+k+'$'
    keys[val] = v

def producePermuterm(token,kgram):
    
    val = [token[i:i+kgram] for i in range(len(token) - kgram+ 1)]
    return val


for i in keys:
    val = producePermuterm(i,3)
    permuterms[i] = val




def Wsearch(query):
    result = []
    q_perm = {}
    q_perm[query] = producePermuterm(query,3)
    for k,v in permuterms.items():
        for qk,qv in q_perm.items():
            for i in v:
                for j in qv:
                    if i == j:
                        result.append(k)
    va = []
    for i in result:
        i = i.replace('$','')
        va.append(i)
    # print(va)

    # print(producePermuterm(query,len(query)))
    filtered = []
    def filtering(va,query):
        fq_perma = producePermuterm(query,len(query))
        for i in va:
            f_perma = producePermuterm(i,len(query))
            
            for j in f_perma:
                for k in fq_perma:
                    if k == j:
                        filtered.append(i)
    filtering(va,query)
    # print(filtered) 

    # print("WildCard Query","DocID")
    index = []
    for i in filtered:
        index.append(dic[i])


    data = {'WildCard Query':filtered,'DocID':index}
    theEnd = pd.DataFrame(data)
    return theEnd


