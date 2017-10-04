#############
#   Carson Witt
#   Independant Study: Intro. to Computer Science - Fundamentals of Programming
#   Mr. Nelson
#   NOTES
#############

### Chapter 4: Conditionals and Recursion ###

#   *4.1 - The Modulus Operator*

#       The modulus oeprator works on integers (and integer expressions)
#       It yields the remainder when the first operand is divided by the second.
#       It is denoted with the percent sign (%)

            quotient = 7 / 3
            print quotient

            OUTPUT: 2

            remainder = 7 % 3
            print remainder

            OUTPUt: 1

#       So 7 divided by 3 is 2 with 1 left over

#       You can also use the modulus operator to check if one number is divisible by the other

            if:
                x % y = 0
                print "x is divisible by y"

#       Also, you can extract the right-most digits or digits from a number.
#       For example, x % 10 yields the right most digit of x (in base 10). Similarly, x % 100 yields the last two digits.

#   *4.2 - Boolean Expressions*

#       a boolean expression is an expression that is either TRUE or FALSE.

#       one way to write a boolean expression is to use the operator ==, which compares two values and produces a boolean value.

            INPUT: 5 == 5
            OUTPUT: True

            INPUT: 5 == 6
            OUTPUT: False

#       below is a list of all the comparison operators:

            x == y          # x is euqal to y
            x != y          # x is not equal to y
            x > y           # x is greater than y
            x < y           # x is less than y
            x >= y          # x is greater than or equal to y
            x <= y          # x is less than or equal to y

#       THINGS TO REMEMBER:

#           (=) is an assignment operator, and (==) is a comparison operator
#           There is NO such thing as =< or =>

#   *4.4 - Conditional Execution*

#       Conditional Statements give us the ability to check conditions and change the behavior of the program accordingly.
#       The simplest form is the 'if' statement:

            if x > 0:
                print "x is positive"

#       The boolean expression after the 'if' statement is called the condition. If it is true, then the intended statement gets executed.
#       Otherwise, nothing happens

#       The 'if' statement is made up of a header and a block of statements:

            HEADER:
                FIRST STATEMENT
                ...
                LAST STATEMENT

#       The header begins on a new line and ends with a colon (:).
#       The indented statements that follow are called a block.
#       The first unindented statement marks the end of the block.
#       A statement block inside a compound statement is called the body of the statement.

#       There is no limit on the number of statements that can appear in the body of an if statement, but there has to be at least one.

#       If you want to have a body with NO statements (if you need a placeholder), use the 'pass' statement, which does nothing.

#   *4.5 - Alternative Execution*

#       The syntax looks like this:

            if x % 2 == 0:
                print x, "is even"
            else:
                print x, "is odd"

#       The alternatives are called 'branches' because they are branches in the flow of execution.

#       As an aside, if you need to check parity (evenness or oddness) often, wrap the code in a function to save time for later:

            def printParity(x):
                if x % 2 == 0:
                    print x, "is even"
                else:
                    print x, "is odd"

#       When you call it, you can provide any integer expression as an argument.

            INPUT: printParity(17)
            OUTPUT: 17 is odd

            INPUT: y = 17
            INPUT: printParity(y+1)
            OUTPUT: 18 is even

#   *4.6 - Chained Conditionals*

#       The syntax looks like this:

            if x < y:
                print x, "is less than", y
            elif x > y:
                print x, "is greater than", y
            else:
                print x, "and", y, "are euqal"

#       elif is an abbreviation of "else if"
#       NOTE: There is no limit to the number of 'elif' statements you can have, but the last branch has to be an else statement:

            if choice == 'A':
                functionA()
            elif choice == 'B':
                functionB()
            elif choice == 'C':
                functionC()
            else:
                print "Invalid choice."

#       Each condition is checked IN ORDER.
#       IMPORTANT: Even if more than one condition is true, only the first true branch executes.

#   *4.7 - Nested Conditionals*

#       One conditional can also be nested within another. We could have written the trichotomy example as follows:

            if x == y:
                print x, "and", y, "are equal"
            else:
                if x < y:
                    print x, "is less than", y
                else:
                    print x, "is greater than", y

#       Logical operators often provide a way to simplify nested conditional statements:

#       ORIGINAL:

            if 0 < x:
                if x < 10:
                    print "x is a positive single digit."

#       ALTERNATE VERSION:

            if 0 < x and x < 10:
                print "x is a positive single digit."

#       BEST VERSION:

            if 0 < x < 10:
                print "x is a positive single digit."
