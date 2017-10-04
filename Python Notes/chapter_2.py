#############
#   Carson Witt
#   Independant Study: Intro. to Computer Science - Fundamentals of Programming
#   Mr. Nelson
#   NOTES
#############

### Chapter 2: Variables, Expressions and Statements ###

#       *VALUES*
#           A number or string (or other thing to be named later) that can be stored in a variable or computed in an expression.

#       values belong to different types: 2 is an integer, and 'Hello, World!' is a string, so-called because it contains a "string" of letters.
#       You (and the interpreter) can identify strings because they are enclosed in quotation marks.

#       If you are not sure what type a value has, the interpreter can tell you:

#       strings = 'str'; integers = 'int'

            INPUT: type("Hello, World!")
            OUTPUT: <type 'str'>

            INPUT: type(17)
            OUTPUT: <type 'int'>

#        numbers with decimal = 'float'

            INPUT: type(3.2)
            OUTPUT: <type 'float'>

#        numbers with a decimal, like the one above, are represented in a format called FLOATING-POINT

#       *VARIABLES*
#           a variable is a name that refers to a value

#       The assignment statement creates new variables and gives them values:

            message = "What's up, Doc?" #For future reference, single ('') and double ("") quotes do the same thing, but if a string needs an apostrophe, enclose it with double quotes.
            n = 17
            pi = 3.14159

#       The print statement also works with variables. See below:

            print message
            print n
            print pi

#       state diagram - A graphical representation of a set of variables and the values to which they refer.

#       *VARIABLE NAMES AND KEYWORDS*

#       Variable Name Rules:
#           They can contain both letters and numbers
#           has to begin with a letter
#           Although it is legal to use uppercase letters, by convention we don't (If you do, remember that case matters).

                Bruce and bruce are different variables.

#           The underscore character (_) can appear in a name. It is often used in names with multiple words:

                my_name = Carson
                price_of_tea_in_china = 7

#           If you give a variable an illegal name, you get a syntax error:

                INPUT: 76trombones = 'big parade'
                OUTPUT: SyntaxError: invalid syntax

#           76trombones is illegal because it does not begin with a letter

                INPUT: more$ = 100000000
                OUTPUT: SyntaxError: invalid syntax

#           more$ is illegal because it contains an illegal character

                INPUT: class = 'Computer Science 101'
                OUTPUT: SyntaxError: invalid syntax

#           class is illegal because it is one of the Python KEYWORDS

#       Python Keywords: define the language's rules and sturcture, and they cannot be used as variable names.
#           There are twenty-nine Python keywords:

            and      | def    | exec    | if         | not   | return
            assert   | del    | finally | import     | or    | try
            break    | elif   | for     | in         | pass  | while
            class    | else   | from    | is         | print | yield
            continue | except | global  | # lambda # | raise |

#       *STATEMENTS*

#         A statement is an instruction that the Python interpreter can execute. We have seen two kinds of statements: print and assignment.

#         When you type a statement on the command line, Python executes it and displays the result, if there is one
#           The result of a print statement is a value
#           Assignment statements don't produce a result

#         If there are mulitple statements, the results appear one at a time as the statements execute.

#       *Evaluating Expressions*

#           An expression is a combination of values, variables, and oeprators. If you type an expression, the interpreter evaluates it and displays the result
#           NOTE: A value all by itself is considered an expression, and so is a variable.

                INPUT: 17
                OUTPUT: 17

#           NOTE: Confusingly, evaluating an expression is not the same thing as printing a value.

                message = 'Hello, World!'
                INPUT: message
                OUTPUT: 'Hello World!'

                INPUT: print message
                OUTPUT: Hello, World!

#           if you evaluate an expression that is a string, the interpreter will leave the quotes
#           if you use a print statement, Python displays the string WITHOUT quotes

#       *Operators and Operands*

#           Operators are special symbols that represent computations like addition and multiplication.
#           The values the operator uses are called operands

#           The symbols +, -, and /, and the use of parenthesis for grouping, mean in Python what they mean in mathematics.
#           The asterisk (*) is the symbol for multiplication
#           and ** is the symbol for exponentiation

#           NOTE: When a variable name appears in the place of an operand, it is replaced with its value before the operation is performed.

#           Division does not always do what you might expect:

                minute = 59
                INPUT: minute/60
                OUTPUT: 0

#           in conventional arithmetic, 59/60 = 0.98333, not 0
#           the reason for this is because Python is performing INTEGER DIVISION

#               When both operands are integers, the reuls MUST also be an integers
#               Integer division ALWAYS rounds down, even in cases where it is very close (0.98333)

#           POSSIBLE SOLUTION: calculate a percentage rather than a fraction:

                INPUT: minute*100/60
                OUTPUT: 98

#           While, the result is still rounded down, the answer is approximately correct.
#           A better alternative is FLOATING-POINT DIVISION, which will be covered in Chapter 3

#       *Operations on Strings*

#           In general, you cannot perform operations on strings, even if the strings look like numbers

#           However, the (+) and (*) operators work on strings:

                fruit = 'banana'
                bakedGood = ' nut bread'
                INPUT: print fruit + bakedGood
                OUTPUT: banana nut bread

                INPUT: print 'Fun'*3
                OUTPUT: 'FunFunFun'

#       *Glossary*

#           value
#               A number or string (or other thing to be named later) that can be stored in a variable or computed in an expression.

#           type
#               A set of values. The type of a value determines how it can be used in expressions. So far, the types you have seen are integers (type int), floating-point numbers (type float), and strings (type string).

#           floating-point
#               A format for representing numbers with fractional parts.

#           variable
#               A name that refers to a value.

#           statement
#               A section of code that represents a command or action. So far, the statements you have seen are assignments and print statements.

#           assignment
#               A statement that assigns a value to a variable.

#           state diagram
#               A graphical representation of a set of variables and the values to which they refer.

#           keyword
#               A reserved word that is used by the compiler to parse a program; you cannot use keywords like if, def, and while as variable names.

#           operator
#               A special symbol that represents a simple computation like addition, multiplication, or string concatenation.

#           operand
#               One of the values on which an operator operates.

#           expression
#               A combination of variables, operators, and values that represents a single result value.

#           evaluate
#               To simplify an expression by performing the operations in order to yield a single value.

#           integer division
#               An operation that divides one integer by another and yields an integer. Integer division yields only the whole number of times that the numerator is divisible by the denominator and discards any remainder.

#           rules of precedence
#               The set of rules governing the order in which expressions involving multiple operators and operands are evaluated.

#           concatenate
#               To join two operands end-to-end.

#           composition
#               The ability to combine simple expressions and statements into compound statements and expressions in order to represent complex computations concisely.

#           comment
#               Information in a program that is meant for other programmers (or anyone reading the source code) and has no effect on the execution of the program.
