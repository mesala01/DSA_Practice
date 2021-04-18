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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def getTextNumbers(): 
    sendersDict ={}
    recieversDict = {}
    for record in texts: # O(n) --> n = len(texts)
        sendersDict[record[0]] = sendersDict.get(record[0], True)
        recieversDict[record[1]] = recieversDict.get(record[1], True)
    return sendersDict, recieversDict

def getCallRecievers():
    recieversDict = {}
    for record in calls: # O(m) --> m = len(calls)
        recieversDict[record[1]] = recieversDict.get(record[1], True)
    return recieversDict

def printPossibleMarketers():
    textSenders, textRecievers = getTextNumbers()
    callRecievers = getCallRecievers()
    telemarketers = set()
    for call in calls: 
        caller = call[0]
        if (not caller in textSenders) and (not caller in textRecievers) and (not caller in callRecievers):
            telemarketers.add(caller)
    telemarketers = sorted(telemarketers) # O(nlogn)
    print(f'These numbers could be telemarketers:')
    for num in telemarketers:
        print(f'{num}')


printPossibleMarketers()