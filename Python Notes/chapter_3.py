#############
#   Carson Witt
#   Independant Study: Intro. to Computer Science - Fundamentals of Programming
#   Mr. Nelson
#   NOTES
#############

# >>> = INPUT

### Chapter 3: Functions ###

#   *3.1 - Function Calls*

#       We've already seen one example of a function call:

            >>> type ("32")
            <type 'str'>

#       This is a "type" function, and it displays the type of a value or variable.
#       The value of the variable (or argument) has to be enclosed in parenthesis.
#       The result of the argument is called the return value.

#       You can also assign the 'type' function to a variable:

            >>> carson = type("22")
            >>> print carson
            <type 'str'>

#      As another example, the 'id' function takes a value or a variable and returns an
#      integer that acts as a unique identifier for the value:

            >>> id(3)
            134882108

            >>> carson = 3
            >>> id(carson)
            134882108

#       Every value has an id, which is a unique number related to where it is stored in the memory of the computer.

#   *3.2 - Type Conversion*

#       Python provides a collection of built-in functions that convert values from one type to another.
#       The 'int' function takes any value and converts it to an integer, if possible, or complains otherwise:

            >>> int("32")
            32
            >>> int("Hello")
            ValueError: invalid literal for int(): Hello

#       int can also convert floating-point values to integers, but remember that it truncates the fractional part:

            >>> int(3.99999)
            3
            >>> int(-2.3)
            -2

#       The 'float' function converts integers and strings to floating-point numbers:

            >>> float(32)
            32.0
            >>> float("3.14159")
            3.14159

#       Finally, the 'str' function converts to type string:

            >>> str(32)
            '32'
            >>> str(3.14149)
            '3.14149'

#       It may seem odd that Python distinguishes the integer value 1 from the floating-point value 1.0.
#       They may represent the same number, but they belong to different types. The reason is that they are represented differently inside the computer.

#   *3.3 - Type Coercion*

#       Returning to the example from the previous chapter, suppose we want to calculate the fraction of an hour that has elapsed.
#       The most obvious expression, 'minute / 60', does integer arithmetic, so the result is always 0, even at 59 minutes past the hour.

#       One solution is to convert minute to floating-point and do floating-point division:

            >>> minute = 59
            >>> float(minute) / 60
            0.983333333333

#       Alternatively, we can take advantage of the rules for automatic type conversion, which is called type coercion.
#       For the mathematical operators, if either operand is a float, the other is automatically converted to a float:

            >>> minute = 59
            >>> minute / 60.0
            0.983333333333

#       By making the denominator a float, we force Python to do floating-point division.

#   *3.4 - Math Functions*

#       Python has a math module that provides most of the familiar mathematical functions.
#       A 'module' is a file that contains a collection of related functions grouped together.

#       Before we can use the functions from a module, we have to import them:

            >>> import math

#       To call one of these functions, we have to use 'dot notation', or the name of the function separated by a dot (period):

            >>> decibel = math.log10 (17.0) # sets 'decibel' to the logarithm of 17, base 10.
            >>> angle = 1.5
            >>> height = math.sin(angle) # finds the sine of the value of the variable angle.

#       NOTE: the other trigonometric functions (cos, tan, etc.) take arguments in radians.
#       To convert from degrees to radians, divide by 360 and multiply by 2*pi.
#       For example, to find the sine of 45 degrees, first calculate the angle in radians and then take the sine:

            >>> degrees = 45
            >>> angle = degrees * 2 * math.pi / 360.0
            >>> math.sin(angle)
            0.707106781187

#   *3.5 - Composition*

#       Just as with mathematical functions, Python functions can be composed, meaning that you use one expression as part of another.
#       For example, you can use any expression as an argument to a function:

            >>> x = math.cos(angle + math.pi/2)

#       This statement takes the value of pi, divides it by 2, and adds the result to the value of angle.
#       The sum is then passed as an argument to the cos function.

#   *3.6 - Adding New Functions*

#       It's possible to add functions that are not built into Python.
#       Creating new functions to solve your particular problems is one of the most useful things about a general-purpose programming language.

#       Function - named sequence of statements that performs a desired operation.

#       The syntax for a function definition is:

            def NAME( LIST OF PARAMETERS ):
                STATEMENTS

#       The list of parameters specifies what information, if any, you have to provide in order to use the new function.

#       Some reasons why creating new functions is effective:

#           Creating a new function gives you an opportunity to name a group of statements. /
#           Functions can simplify a program by hiding a complex computation behind a single command and by using English words in place of arcane code.

#           Creating a new function can make a program smaller by eliminating repetitive code. /
#           For example, a short way to print nine consecutive new lines is to call threeLines three times.

#   *3.7 - Definitions and Use*

#       Pulling together the code fragments from Section 3.6, the whole program looks like this:

            def newLine():
              print

            def threeLines():
              newLine()
              newLine()
              newLine()

            print "First Line."
            threeLines()
            print "Second Line."

#       As you might expect, you have to create a function before you can execute it.
#       In other words, the function definition has to be executed before the first time it is called.

#   *3.8 - Flow of Execution*

#       Flow of Execution - the order in which statements are executed
#           Statements are executed one at a time, in order from top to bottom

#       Function definitions do not alter the flow of execution of the program,
#       but remember that statements inside the function are not executed until the function is called.

#       Although it is not common, you can define one function inside another.
#       In this case, the inner definition isn't executed until the outer function is called.

#       Function calls are like a detour in the flow of execution.
#       Instead of going to the next statement, the flow jumps to the first line of the called function, executes all the statements there, and then comes back to pick up where it left off.

#       (NOTE): IN CONCLUSION: When you read a program, don't read from top to bottom. Instead, follow the flow of execution.

#   *3.9 - Parameters and Arguments*

#       Some functions take more than one argument. For example, pow takes two arguments, the base and the exponent.
#       Inside the function, the values that are passed get assigned to variables called parameters.

#       Here is an example of a user-defined function that has a parameter:

            def printTwice(bruce):
              print bruce, bruce

#       This function takes a single argument and assigns it to a parameter named bruce.
#       The value of the parameter (at this point we have no idea what it will be) is printed twice, followed by a newline.
#       The name bruce was chosen to suggest that the name you give a parameter is up to you, but in general, you want to choose something more illustrative than bruce.

#       The function 'printTwice' works for any type that can be printed:

            >>> printTwice('Spam')
            Spam Spam

            >>> printTwice(5)
            5 5

            >>> printTwice(3.14159)
            3.14159 3.14159

#       In the first function call, the argument is a string. In the second, it's an integer. In the third, it's a float.

#   *3.10 - Variables and Parameters Are Local*

#       When you create a local variable inside a function, it only exists inside the function, and you cannot use it outside. For example:

            def catTwice(part1, part2):
              cat = part1 + part2
              printTwice(cat)

#       This function takes two arguments, concatenates them, and then prints the result twice.
#       We can call the function with two strings:

            >>> chant1 = "Pie Jesu domine, "
            >>> chant2 = "Dona eis requiem."
            >>> catTwice(chant1, chant2)
            Pie Jesu domine, Dona eis requiem. Pie Jesu domine, Dona eis requiem.

#       When catTwice terminates, the variable cat is destroyed. If we try to print it, we get an error:

            >>> print cat
            NameError: cat

#       Parameters are also local. For example, outside the function printTwice, there is no such thing as bruce.
#       If you try to use it, Python will complain.

#   *3.11 - Stack Diagrams*

#       To keep track of which variables can be used where, it is sometimes useful to draw a stack diagram.
#       Like state diagrams, stack diagrams show the value of each variable, but they also show the function to which each variable belongs.

#       Each function is represented by a frame. A frame is a box with the name of a function beside it and the parameters and variables of the function inside it.
#       The stack diagram for the previous example looks like this (go to link):

            http://www.greenteapress.com/thinkpython/thinkCSpy/html/illustrations/stack.png

#       if we try to access cat from within printTwice, we get a NameError:

            Traceback (innermost last):
              File "test.py", line 13, in __main__
                catTwice(chant1, chant2)
              File "test.py", line 5, in catTwice
                printTwice(cat)
              File "test.py", line 9, in printTwice
                print cat
            NameError: cat

#       This list of functions is called a 'traceback'. It tells you what program file the error occurred in, and what line, and what functions were executing at the time.
#       It also shows the line of code that caused the error.

#       Notice the similarity between the traceback and the stack diagram. It's not a coincidence.
