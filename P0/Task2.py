"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('./P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('./P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
longestTimeSpent = 0
callsDict = {}
telNum = ""
for call in calls:
    caller = call[0]
    reciever = call[1]
    duration = int(call[len(call) - 1])
    if callsDict.get(caller):
        callsDict[caller] = callsDict.get(caller) + duration
    else:
        callsDict[caller] = duration

    if callsDict.get(reciever):
        callsDict[reciever] = callsDict.get(reciever) + duration
    else:
        callsDict[reciever] = duration

    if callsDict[caller] > longestTimeSpent: 
        longestTimeSpent = callsDict[caller]
        telNum = caller
    elif callsDict[reciever] > longestTimeSpent :
        longestTimeSpent = callsDict[reciever]
        telNum = reciever

print(f'{telNum} spent the longest time, {longestTimeSpent} seconds, on the phone during September 2016.')
