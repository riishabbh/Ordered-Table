# Current year, change at January 1, {year + 1}
year = 2021

"""
[
    [name3, DOB (year), ID (10 characters)],
    [name5, DOB (year), ID (10 characters)],
    [name1, DOB (year), ID (10 characters)],
    [name2, DOB (year), ID (10 characters)],
    [name4, DOB (year), ID (10 characters)]
]

Into:

+-------+------+---------------+
| Name1 | year | ID (10 chars) |
+-------+------+---------------+
| Name2 | year | ID (10 chars) |
+-------+------+---------------+
| Name3 | year | ID (10 chars) |
+-------+------+---------------+
| Name4 | year | ID (10 chars) |
+-------+------+---------------+
| Name5 | year | ID (10 chars) |
+-------+------+---------------+

And everything will be sorted by name, year, or ID (depending on user input)

With one space padding around everything.
(for names it will be one space around longest name,
and one space to the left of other names.)
"""

import random

# Gets the user input >>>
def getMainLst(rows):

    global mainLst
    mainLst = []

    for row in range(rows):
        lst = []

        name = str(input("\nEnter name of person {}: ".format(row + 1)))
        # Check if any numbers are in name
        while not name.replace(' ', '').isalpha():
            print("That is not a valid name,\nMake sure to only use English characters \n(abcdefghijklmnopqrstuvwxyz)")
            name = str(input("Enter name of person {}: ".format(row + 1)))
        lst.append(name.lower())

        # Year of birth has to be a four digit positive integer.
        yob = input("Enter Year of Birth of person {}: ".format(row + 1))
        if yob.isnumeric() and (year <= int(yob) or int(yob) < 1900):
            print("You can time travel? Teach me how!\nTill then, you will have to retype the input, we don't accept time travellers \n(so please enter a number between 1900 and {str(year)}\n")
            # Does not follow while loop - makes loop repeat.
            yob = "a"

        while not (len(yob) == 4 and yob.isnumeric()):
            print("You are entering something other than a four digit positive integer,\nor perhaps you are a time traveller.\nPlease enter a positive integer less than the current year.")
            yob = input("Enter Year of Birth of person {}: ".format(row + 1))
            # No one is that old!
            if yob.isnumeric() and (year <= int(yob) or int(yob) < 1900):
                # Does not follow while loop - makes loop repeat.
                print(f"You can time travel? Teach me how!\nTill then, you will have to retype the input, we don't accept time travellers \n(so please enter a number between 1900 and {str(year)}")
                yob = 'a'
        lst.append(str(yob))

        # This should be enough for the world population
        # Made this a random because I didn't want to input so much.
        userID = str(random.randint(1, 9999999999)).zfill(10)
        print(f"{name.title()}'s ID is {userID}.")
        lst.append(userID)

        # Finally append lst to mainLst,
        mainLst.append(lst)
# <<<

################################

# Gets the main list (input) >>>
rowInput = input("How many rows do you want: ")
if rowInput.isnumeric() and int(rowInput) > 100:
    print("That's a lot of rows, are you sure you will be able to do it?\nBut hey, I'm not stopping you.")
while not rowInput.isnumeric(): # - and . not allowed.
    print("It appears you entered something other than a positive integer,\nPlease follow the given format.")
    rowInput = input("How many rows do you want: ")
    if rowInput.isnumeric() and int(rowInput) > 100:
        print("That's a lot of rows, are you sure you will be able to do it?\nBut hey, I'm not stopping you.")
rowInput = int(rowInput)

getMainLst(rowInput)
# At this point, mainLst exists.
# <<<

# We have to get the longest name
def getLongestName(listOnames):
    global longest
    longest = 0
    for row in range(len(listOnames)):
        if len(listOnames[row][0]) > longest:
            longest = len(listOnames[row][0])

getLongestName(mainLst)

# Make the bars
bar = "+{}+------+------------+".format("-" * (longest + 2))

################################

# Now that we have the main list input, we can sort it out.
# But first we must see what the user wants to sort by.

# Gets the input for what the user wants to sort by >>>
sortInput = input("\nDo you want to sort by name, year of birth, or ID?\nEnter 'name', 'yob', or 'ID':  ")
while sortInput.lower() not in ('name', 'yob', 'id'):
    print("It appears you entered something different from the asked input,\nPlease follow the given format. (Keep in mind it is case insensitive!)")
    sortInput = input("Do you want to sort by name, year of birth, or ID?\nEnter 'name', 'yob', or 'ID':  ")
sortInput = sortInput.lower()
# <<<

sortConvert = {
    'name' : 0,
    'yob' : 1,
    'id' : 2
}

sortValue = sortConvert[sortInput]

################################

# Using key functions
# https://docs.python.org/3/howto/sorting.html#key-functions
sortedLst = sorted(mainLst, key = lambda sortBy : sortBy[sortValue])
# Now our list is sorted, now we have to use sortedLst

################################

def makeTable(finalLst):
    # Now we just have to make the table (use sortedLst as finalLst)
    for row in range(len(finalLst)):
        spacesCount = longest - len(finalLst[row][0])
        name = finalLst[row][0].title()
        yob = finalLst[row][1]
        idValue = finalLst[row][2]
        print(bar)
        print(f"| {name}{' ' * spacesCount} | {yob} | {idValue} |")
    print(bar)

makeTable(sortedLst)
