ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that"

stuff = ten_things.split(' ')
more_stuff = ["day", "night", "song", "frisbee", "Corn", "Banana", "Girl", "boy"]

while len(stuff) !=10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now" % len(stuff)

print "There we go", stuff

print "Let's do some things with stuff"

print stuff[1]
print stuff[-1] #neat
print stuff.pop()
print ' '.join(stuff) #cool
print '#'.join(stuff[3:5])
