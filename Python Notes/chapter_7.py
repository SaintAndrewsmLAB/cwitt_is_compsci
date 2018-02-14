#############
#   Carson Witt
#   Independent Study: Intro. to Computer Science - Fundamentals of Programming
#   Mr. Nelson
#   NOTES
#############

### Chapter 7: Strings ###

#   *7.1 - A Compound Data Type*

#       Strings are qualitatively different from the other two types because they are made up of smaller pieces--characters.

#       Types that comprise smaller pieces are called compound data types.
#       Depending on what we are doing, we may want to treat a compound data type as a single thing, or we may want to access its parts.
#       This ambiguity is useful.

#       The bracket operator selects a single character from a string.

            >>> fruit = "banana"
            >>> letter = fruit[1]
            >>> print letter

#       The expression fruit[1] selects character number 1 from fruit. The variable letter refers to the result. When we display letter, we get a surprise:

            a

#       To get the first letter of a string, you just put 0, or any expression with the value 0, in the brackets:

            >>> letter = fruit[0]
            >>> print letter
            b

#   *7.2 - Length*

#       The len function returns the number of characters in a string:

            >>> fruit = "banana"
            >>> len(fruit)
            6

#       To get the last letter of a string, you might be tempted to try something like this:

            length = len(fruit)
            last = fruit[length]       # ERROR!

#       That won't work. It causes the runtime error "IndexError: string index out of range".
#       The reason is that there is no 6th letter in "banana". Since we started counting at zero, the six letters are numbered 0 to 5.
#       To get the last character, we have to subtract 1 from length:

            length = len(fruit)
            last = fruit[length-1]

#       Alternatively, we can use negative indices, which count backward from the end of the string.
#       The expression fruit[-1] yields the last letter, fruit[-2] yields the second to last, and so on.

#   *7.3 - Traversal And The 'for' Loop*

#       A lot of computations involve processing a string one character at a time.
#       Often they start at the beginning, select each character in turn, do something to it, and continue until the end.
#       This pattern of processing is called a traversal. One way to encode a traversal is with a while statement:

            index = 0
            while index < len(fruit):
              letter = fruit[index]
              print letter
              index = index + 1

#   *7.4 - String Slices*

#       A segment of a string is called a slice. Selecting a slice is similar to selecting a character:

            >>> s = "Peter, Paul, and Mary"
            >>> print s[0:5]
            Peter
            >>> print s[7:11]
            Paul
            >>> print s[17:21]
            Mary

#       The operator [n:m] returns the part of the string from the "n-eth" character to the "m-eth" character, including the first but excluding the last.
#       This behavior is counterintuitive; it makes more sense if you imagine the indices pointing between the characters

#       If you omit the first index (before the colon), the slice starts at the beginning of the string. If you omit the second index, the slice goes to the end of the string. Thus:

            >>> fruit = "banana"
            >>> fruit[:3]
            'ban'
            >>> fruit[3:]
            'ana'

#   *7.5 - String Comparison*
