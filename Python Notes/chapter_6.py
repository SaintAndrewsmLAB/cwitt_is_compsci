#############
#   Carson Witt
#   Independent Study: Intro. to Computer Science - Fundamentals of Programming
#   Mr. Nelson
#   NOTES
#############

### Chapter 6: Iteration ###

#   *6.1 - Multiple Assignment*

#       It is legal to make more than one assignment to the same variable.
#       A new assignemnt makes an existing variable refer to a new value. (and stop referring to an old value)

            bruce = 5
            print bruce,
            bruce = 7
            print bruce

            OUTPUT: 5, 7

#       The output is 5, 7 because the value of bruce changes in the middle of the program.

#       NOTE: The comma at the end of the first print statement suppresses the newline after the output,
#           Which is why both outputs appear on the same line.

#       FURTHERMORE: In python, an assignment statement can make two variables equal, but they don't have to stay that way:

            a = 5
            b = a # a and b are now equal
            a = 3 # a and b are no longer equal

#       The third line changes the value of a but does not change the value of b, so they are no longer equal.

#   *6.2 - The 'While' Statement*

#       Here's what a block of code names 'Countdowm' looks like with a while statement:

            def countdown(n):
                while n > 0:
                    print n
                    n = n - 1
                print "Blastoff!"

#       Code in words: "While n is greater than 0, continue displaying the value of n and then reducing the value of n by 1. When you get to 0, display the word Blastoff!"

#       This type of flow is called a 'loop' because the third step loops back around to the top.
#       NOTE: If the condition if false the first time through the loop, the statements inside the loop are never executed.

#       If the body of the loop does not change that value of the variable, the loop will never terminate. This is called an "infinite loop"

#   *6.5 - Encapsulation and Generalization*

#       Encapsulation is the process of wrapping a piece of code in a function, allowing you to take advantage of all the things functions are good for.
#       You have seen two examples of encapsulation: printParity in Section 4.5; and isDivisible in Section 5.4.

#       Generalization means taking something specific, such as printing the multiples of 2, and making it more general, such as printing the multiples of any integer.

#       This function encapsulates the previous loop and generalizes it to print multiples of n:

            def printMultiples(n):
              i = 1
              while i <= 6:
                print n*i, '\t',
                i = i + 1
              print

#       To encapsulate, all we had to do was add the first line, which declares the name of the function and the parameter list.
#       To generalize, all we had to do was replace the value 2 with the parameter n.

#       If we call this function with the argument 2, we get the same output as before.
#       With the argument 3, the output is:

            3      6      9      12     15     18

#       With the argument 4, the output is:

            4      8      12     16     20     24

#       By now you can probably guess how to print a multiplication table by calling printMultiples repeatedly with different arguments.
#       In fact, we can use another loop:

            i = 1
            while i <= 6:
              printMultiples(i)
              i = i + 1

#       Notice how similar this loop is to the one inside printMultiples. All we did was replace the print statement with a function call.

#       The output of this program is a multiplication table:

            1      2      3      4      5      6
            2      4      6      8      10     12
            3      6      9      12     15     18
            4      8      12     16     20     24
            5      10     15     20     25     30
            6      12     18     24     30     36

#   *6.9 - Functions*

#       A few times now, we have mentioned "all the things functions are good for." By now, you might be wondering what exactly those things are.
#       Here are some of them:

#           *Giving a name to a sequence of statements makes your program easier to read and debug.
#           *Dividing a long program into functions allows you to separate parts of the program, debug them in isolation, and then compose them into a whole.
#           *Functions facilitate both recursion and iteration.
#           *Well-designed functions are often useful for many programs. Once you write and debug one, you can reuse it.
