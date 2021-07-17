import csv
from nltk import RegexpParser, pos_tag, word_tokenize

# Insert CSV File Path
file = '/Users/mattolszak/Desktop/Python NLP/Course Data/NEW_master_graded_comments_2019_Fall_ST.csv'

# Read the CSV File
reader = csv.reader(open(file), delimiter=',')

# Create an empty dictionary
dict = {}
# Parse through each row creating Key:Pair values of student as Key and response as Value
with open(file, newline='') as csvfile:
    data = csv.reader(csvfile)
    for row in reader:
        tagged1 = pos_tag(word_tokenize(row[0]))
        row[0] = tagged1
        dict = {row[1]: row[0]}
        # Print out the Dictionary
        print(dict)
