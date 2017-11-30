x = input("What number would you like to take the multiplication table out to? ")

def printMultiples(n):
    i = 1
    while i <= x:
        print n*i, '\t',
        i = i + 1
    print

i = 1
while i <= x:
    printMultiples(i)
    i = i + 1
