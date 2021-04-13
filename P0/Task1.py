"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('./P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('./P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
tel_set = set()
for record in texts:
    tel_set.add(record[0])
    tel_set.add(record[1])
for record in calls:
    tel_set.add(record[0])
    tel_set.add(record[1])
print(f'There are {len(tel_set)} different telephone numbers in the records.')

