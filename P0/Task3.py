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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.


Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# function to get area code from telephone number
def getTelNumCode(num): # O(1)
  if num[0] == "(":
    num = f'{num.split(")")[0]})'
  elif num[:3] == "140":
    num = "140"
  else:
    num = num[:4]
  return num

#check if number starts with "(080)"
def isBangaloreNum(num): # O(1)
  if num[:5] =="(080)":
    return True
  return False

# Gets the list of all area codes called by Banglore callers
def getAreaCodeList():
  areaCodes = []
  for call in calls: #O(n)
    caller = call[0]
    if isBangaloreNum(caller): # O(1)
      areaCode = getTelNumCode(call[1]) #O(1)
      areaCodes.append(areaCode)
  return areaCodes

# gets the percentage of Banglore calls using the getAreacodelist (list of all area codes called by Banglore callers )
def getPercOfBangloreCalls():
  codes = getAreaCodeList()
  totalCalls = len(codes)
  bangCodeCount = 0
  for code in codes: # O(n)
    if code == "(080)":
      bangCodeCount += 1
  return (bangCodeCount*100 /totalCalls)

# Prints string result for both part 1 and part 2
def printResult():
  areaCodes = set(getAreaCodeList()) # O(n)
  areaCodes = sorted(areaCodes) # O(nlogn)
  callPerc = round(getPercOfBangloreCalls(), 2) 
  # print the area code list for Banglore callers
  print("The numbers called by people in Bangalore have codes:")
  for code in areaCodes:
    print(code)

  #Print the percentage
  print(f"{callPerc} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


printResult()