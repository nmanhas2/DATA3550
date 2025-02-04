"""
Algorithm: 

-a step-by-step description of how to solve a 
problem

-A sequence (the order mattering) of actions to
take to accomplish the given task

-An algorithm is a set of instructions written
in a sequence that achieves a goal

-For complex problems, software developers write
and algorithm before they attempt to write a 
computer program

-Describes a sequnce of steps that is:

-Unambiguous - no assumptions are required to
execute the algorithm. the algorithm uses 
precise instructions

-Executable - can be carried out in practice

-Terminating - Eventually come to an end or
halt
"""

"""
Computer programs:

-Tells a computer the seuqnce of steps neede
to complete a specific task

-The program consists of a very large number
of primitive instructions

-Computers can carry out a wide range of tasks
because they can execute different programs. 
Each program is designed to direct the computer
to work on a specific task

-Programming - The act of designing, implementing
, and test computer programs
"""

"""
Hardware:

-Consists of the physical elements in a computer
system.

-The central processing unit (CPU) performs 
program control and data processing

-Storage devices include (RAM) and secondary
storage (Hard dish, flash drives, CD/DVD drive)

-Input/output devices allow the user to 
interact with the computer (mouse, keyboard, etc)
"""

"""
The CPU:

-CPU has two components, the control unit and
the arithmetic logic unit (ALU)

Control unit -  
- directs operation of the processor. All 
computer resources are managed by the control unit
-It reads and interprets instructions and 
determines the sequence for processing data
-It provides timing and control signals

Arithmetic logic unit - 
-Contains circuitry to perform calculations and
do comparisons
-Workhose portion of the computer and its job is
to do precisely what the control unit tells it to
"""

"""
Storage:

Primary Storage:
-Composed of memory chips (electronic circuits)
that can store data as long as it is provided
electric power)

Secondary storage:
-Provides aa slower, less expensive storage that
persists: the data persists without electric
power

-Computers store both and and programs

-The data and program are located in secondary
storage and loaded into memory when the program
is executed
"""

"""
Memory:

-Memory is a table of cells all the same size,
one byte, and each containing a unique address
beginning with 0
"""

"""
Executing a Program

-Program instructions and data (text, numbers,
visual or audio) are stored in digital format

-The CPU runs the program one instruction at a
time. The program may react to user input

-The instructions and user input guide the 
program execution. The CPU reads data (including
user input), modifies it, and writes it back to
memory, the screen, or secondary storage
"""

"""
Software:

-Typically realized as an application program

-Sequence of instructions and decisions 
implemented in some language and translated
to a form that can be executed or run on the 
computer

-Computers execute very basic instructions in 
rapid succession. The basic instructions can be
grouped together to perform complex tasks

-Programming is the act of designing and
implementing computer programs
"""

"""
Python Language:

-Python is interpreted, making it easier to 
develop and test short programs

-Executed by the Python interpreter

-Can use them in an integrated development
environment (IDE) or using a text editor

-Compiled languages examine your entire program
at compile time, and are able to warn you about
a whole class of errors prior to execution

-Python interprets your script line by line
as it execute. It will stop executing when it
encounters an error. This is an interpreted
language

-Object-oriented language
"""

"""
Errors:

-Compile-time error: error is violation of the
programming language rules, that is detected by
the computer

-A run-time error causes a program to take an
action that the programmer did not intend
"""

"""
Types:

-You can find out the type by using the 'type'
command

-Type casting: 

-int() constructs and int from an
integer literal, float literal (removes decimals)
, or a string literal (assuming it represents a
whole number)

-float() constructs a float number from an int
literal, float literal, or a string literal (
assuming that the string represents a float or
an int)

-str() constructs a string from a wide variety
of data types, invluding strings, integer literals
, and float literals
"""

"""
Variables

-named storage location in a computer program

-variables refer to objects

-constant is a variable whose value should not 
be changed after it's assigned an initial value

-you must define a variable before you use it
"""

"""
Arithmetic:

-Expressions like +, -, *, **, /, //, %

- //(floor division) is a normal division except
that it returns the largest possible integer.
This integer is either less than or equal to the
normal division result

-When you do operations with an integer and a
floating point number, the result is a floating
point value
"""

"""
Functions:

-a collection of programming instructions that
carry out a particular task

-When calling a function you must provide the
correct number of arguments

-Built in math functions: abs(x), round(x),
round(x, n), max(x1,x2,...,xn), min(x1,x2,...,xn)
"""

"""
Python Libraries (Module)

-A collection of code, written and compiled by
someone else, that is ready for you to use in
your program

-A standard library is a library that is 
considered part of thhe lanuage

-Python's standard library is organized into
modules

-Built-in functions are a small set of functions
that are defined as a part of the Python language

-Ex: from math import sqrt

-Selected functions in the math module: sqrt(x),
trunc(x) -> truncates floating point value x
to and int, cos(x), sin(x), tan(x), exp(x) ->e^x,
degrees(x), radians(x), log(x), log(x, base)
"""

"""
Strings:

-Consists of characters: letters, numbers,
punctuation, spaces, etc

-A string is a sequence of characters

-To include quotes in strings you can:

-print("'Hello'") 

-print("\"Hello\"")

-Escape sequence: \something

-You can use len() function to determine the
length of a string. String length 0 is an empty
string

-Slicing: name[0:4] -> the first number means 
the index (starting point), and the second number
means the length from the index to the last element

-Stride: name[::3] -> basically means we're
getting every third character, starting an index
1 (name[0])

-Using '+' to concatenate is called operator
overloading

-Python uses unicode encoding. Character values 
are stored as numbers
"""

"""
String Methods:

-An object is a software entity that represents
a value with certain behavior

-The behavior of an object is given through its
methods

-A method is a collection of programming instructions
to carry out a specific task. Unlike a function,
which is a standalone oepration, a metho can only
be applied to an object of the type for which it
was defined

-.find(): finds the index of a string within a
string. Returns -1 if it's not in the string

-.lower(): lowercase version of string s

-.upper(): upper case version of s

-.replace(old, new): new version of string is
in which every occurrence of the substring 'old'
is replaced by the string 'new'
"""