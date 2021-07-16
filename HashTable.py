import csv
from nltk import RegexpParser, pos_tag, word_tokenize

# Insert CSV File Path
File = open("/Users/mattolszak/Desktop/Python NLP/Course Data/NEW_master_graded_comments_2019_Fall_ST.csv", "r")
file = '/Users/mattolszak/Desktop/Python NLP/Course Data/NEW_master_graded_comments_2019_Fall_ST.csv'

# Read the CSV File
reader = csv.reader(File, delimiter=',')

# Create an empty dictionary
dict = {}
# Parse through each row creating Key:Pair values of student as Key and response as Value
with open(file, newline='') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        tagged1 = pos_tag(word_tokenize(row['Response']))
        chunk1 = RegexpParser("""
                                NP: {<DT>?<JJ>*<NN>}
                                P: {<IN>}
                                V: {<V.*>}
                                PP: {<P> <NP>}
                                VP: {<V> <NP|PP>*}
                                """)
        output = chunk1.parse(tagged1)
    for rows in reader:
        dict = {rows[1]: output for rows in reader}
    # Print out the Dictionary
    print(dict)
