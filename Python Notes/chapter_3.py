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
