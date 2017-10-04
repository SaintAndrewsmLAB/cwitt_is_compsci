#############
#   Carson Witt
#   Independant Study: Intro. to Computer Science - Fundamentals of Programming
#   Mr. Nelson
#   loops.py
#############

# Number 1

for i in range(2,10):
    print 1.0/i    
print "Done."

# Number 2

n = input("Type a number: ")
if n > 0:
    while n >= 0:
        print n
        n = n - 1
    print "Done."
else:
    while n <= 0:
        print n
        n = n + 1
    print "Done."

# Number 3

print "This Is An Exponent Calculator"
print "------------------------------"
base = input("Base: ")
exp = input("Exponent: ")

print base,"^",exp,"is",base**(exp)

# Number 4

num = input("Please enter a number that is divisible by 2: ")
while num % 2 != 0:
    num = input("Close, but no cigar. Let's try that again champ: ")
if num % 2 == 0:
    print "Good Job!"

    
