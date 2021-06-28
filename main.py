""" FEEL FREE TO GIVE SUGGESTIONS ON HOW TO IMPROVE THIS :D """

"""
[
    [name3, DOB (year), ID (10 characters)],
    [name5, DOB (year), ID (10 characters)],
    [name1, DOB (year), ID (10 characters)],
    [name2, DOB (year), ID (10 characters)],
    [name4, DOB (year), ID (10 characters)]
]

Into:

+-----------+------+------------------+
| Name      | year | ID (10 chars)    |
+-----------+------+------------------+
| Name      | year | ID (10 chars)    |
+-----------+------+------------------+
| Name      | year | ID (10 chars)    |
+-----------+------+------------------+
| Name      | year | ID (10 chars)    |
+-----------+------+------------------+
| Name      | year | ID (10 chars)    |
+-----------+------+------------------+

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
            name = str(input("Enter name of person {}: ".format(row + 1)))
        lst.append(name.lower())

        # Year of birth has to be a four digit positive integer.
        yob = input("Enter Year of Birth of person {}: ".format(row + 1))
        if yob.isnumeric() and int(yob) < 1900:
            # Does not follow while loop - makes loop repeat.
            print("\tThat person cannot be that old!")
            yob = "a"

        while not (len(yob) == 4 and yob.isnumeric()):
            yob = input("Enter Year of Birth of person {}: ".format(row + 1))
            # No one is that old!
            if yob.isnumeric() and int(yob) < 1900:
                # Does not follow while loop - makes loop repeat.
                print("\tYou aren't that old!")
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
while not rowInput.isnumeric():
    rowInput = input("How many rows do you want: ")
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
