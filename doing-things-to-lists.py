# define a string of text
ten_things = 'Apples Oranges Crows Telephone light Sugar'

print("Hol up there are not 10 things in that list lets fix that.")

# split the string of text by blank spaces
stuff = ten_things.split()

# define another list called more_stuff
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# append elements to stuff until there are 10 elements
while len(stuff) != 10:
    # removing an element from more_stuff and storing it in next_one
    next_one = more_stuff.pop()

    print("Adding: ", next_one)

    # adding the value of next_one to stuff(specifically the list)
    stuff.append(next_one)

    print("There are {0} items now.", len(stuff))
    print("There we go: ", stuff)

# experimentation with modyfing the list while following the appropriate parameters
print("Let's do some things with stuff.")

# printing the value of element 1
print(stuff[1])

# printing the value of last element
print(stuff[-1])

# Removing the last element of stuff and printing
print(stuff.pop())

# adding spaces to stuff and printing them as a single string
print(' '. join(stuff))

# adding spaces to the specific elements(elements 3 and 4 with a space between them) of stuff and printing them as a single string
print(' '.join(stuff[3:5])) # SLICING
