# This code compares a students review by inputting a csv file and comparing a students responses
## Example Student 1 Response 1 to Student 1 Resposne 2. The reason for this is to determine if 
### the responses left by the student are actually written by them, and not by another student.
#### THIS IS A WORK IN PROGRESS AND A CODE WRITTEN BY MATTHEW OLSZAK IN COLLABORATION WITH ZACHARIAH BEASLEY PhD

import pandas as pd
from nltk import pos_tag, word_tokenize
from difflib import SequenceMatcher
import string

# Make dataset using panda to read in the CSV file
dataset = pd.read_csv(r'/Users/mattolszak/Desktop/Python NLP/Course Data/NEW_master_graded_comments_2019_Fall_ST.csv')

HashTable ={}
for k in range(1,43):
    # Student Response is name of dictionary
    stureslist = []
    for i in dataset[dataset['Student 1'] == 'Student ' + str(k)]['Response']:
        stures = ''
        tags = pos_tag(word_tokenize(str(i).translate(str.maketrans('', '', string.punctuation))))
        for j in tags:
            stures +=j[1]
            stures += ' '
        stureslist.append(stures)
    HashTable['Student '+str(k)]=stureslist

print(HashTable.keys())

print(dict(list(HashTable.items())[:1]))


# Displaying the Hash Table as a pandas dataframe
shash = {}
for key, value in HashTable.items():
    ls = []
    for i in range(0, len(value) - 1, 2):
        similarity = SequenceMatcher(None, value[i], value[i+1]).ratio()
        ls.append(similarity)
        ls.append(similarity)
        shash[key] = ls

# Hash Table after POS Response
df1 = pd.DataFrame(HashTable.items())
df1.columns = ['Students', 'Responses Tags']
print(df1.head())


# Hash Table with POS and Similarity Score
df2 = pd.DataFrame(shash.items())
df2.columns = ['Students', 'Similarity Ratio']
df2['Responses Tags'] = df1['Responses Tags']

df2= df2[['Students', 'Responses Tags', 'Similarity Ratio']]


print("Hash Table after applying similarity ratio to the POS")
print(df2.head())
