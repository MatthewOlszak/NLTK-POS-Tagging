import csv
# Insert CSV File Path
File = open("/Users/mattolszak/Desktop/Python NLP/Course Data/NEW_master_graded_comments_2019_Fall_CG.csv", "r")
# Read the CSV File
reader = csv.reader(File, delimiter=',')
# Create an empty dictionary
dict = {}
# Parse through each row creating Key:Pair values of student as Key and response as Value
for rows in reader:
    dict = {rows[1]:rows[0] for rows in reader}
# Print out the Dictionary
print(dict)
