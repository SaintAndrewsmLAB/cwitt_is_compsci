#############
#   Carson Witt
#   Independant Study: Intro. to Computer Science - Fundamentals of Programming
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
