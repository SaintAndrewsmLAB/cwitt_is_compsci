#############
#   Carson Witt
#   Independant Study: Intro. to Computer Science - Fundamentals of Programming
#   Mr. Nelson
#   NOTES
#############

### Chapter 4: Conditionals and Recursion ###

#   *4.12 - Keyboard Input*

#       Python has build in functions that get input from the user/keyboard. The simplest function is called 'raw_input'

            prompt = raw_input("What is your favorite number?")

#       If you want a integer response, use the 'input' functions

            number = input(prompt)

#       If the user types a string of digits, it is converted to an integer and assigned to speed. Unfortunately, if the user types a character that is not a digit, the program crashes:

            >>> number = input(prompt)
            What is your favorite number?
            Five!
            SyntaxError: invalid syntax

#       To avoid this kind of error, it is generally a good idea to use raw_input to get a string and then use conversion functions to convert to other types.
