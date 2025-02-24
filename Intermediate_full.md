---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.7
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
ARC course "Coding with Python" (Intermediate level)
====================================================
![icons8-python-48.png](images/icons8-python-48.png)
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
Welcome to our ARC course "Coding with Python" (Intermediate level).

Some general information on how the course will run:

* The course will run for three hours from 09:00 to 12:00. We plan a coffee break between 2 parts at around 10:30 for ~10-15 min.

* This material builds upon the knowledge acquired in the previous Beginner level course.

* Each topic will be presented wih code demonstrations followed by practical exercises.

* We are happy to answer any questions during the course and to help during the exercises.

Upon completion of the course, please, don't forget to scan the activity QR code to record your attendance.

Enjoy coding with Python!
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## Set up your Python environment
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
There are several option how you can read and run this Jupyter notebook:
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
#### <ins>Option 1 (preferred)</ins>: The Jupyter Notebook server set up by Daniel Maitre from the Physics department
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
1) Log in with your CIS account (loading process can take some time):
   - https://notebooks.dmaitre.phyip3.dur.ac.uk/arc

2) Upload this tutorial course
   - Go to the repository: https://github.com/DurhamARC-Training/Intermediate-Python
   - Download `pull_files_from_repo.py` file into your environment and upload it to the Jupyter Notebook server
   - Open the terminal on the Jupyter Notebook server and execute `python pull_files_from_repo.py`. It'll upload the entire tutorial from GitHub to the server
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
#### <ins>Option 2 (if the previous one doesn't work)</ins>: Google Colab (https://colab.research.google.com)
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
1) Log in to Google Colab, for example, with your Google account
2) Open our tutorial by specifying its GitHub URL (https://github.com/DurhamARC-Training/Intermediate-Python) and selecting the notebook (`Intermediate.ipynb`)
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
#### <ins>Option 3 (if you want to run locally)</ins>: Local Python environment
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
**Install Python**

---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
<ins>On Windows</ins>:
  1) Go to https://www.python.org/downloads/ and choose the latest stable installer for Windows (e.g., "Windows installer (64-bit)")
  2) During installation, make sure to check the box “Add Python to PATH” so you can use Python from any command prompt
  3) After installation finishes, open a new Terminal (Command Prompt or PowerShell) and type:
     
     `python --version`

     This should confirm that Python has been installed successfully
  5) *Alternatively* 👉 You can install the *Anaconda* distribution from https://www.anaconda.com/products/distribution, which includes Python and a variety of data-science packages by default

---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
<ins>On Linux</ins> (Ubuntu/Debian-based):
  1) Open a terminal
  2) Run:
     
     `sudo apt-get update`
     
     `sudo apt-get install python3 python3-pip`
     
     (Adjust to *python* or *python3* depending on your distribution)
  4) Confirm your installation by running:

     `python3 --version`
     
  6) *Note* 📝 For Fedora or other distributions, replace `apt-get` with `yum`, `dnf`, or your distro’s package manager
  7) *Alternatively* 👉 You can also install *Anaconda* if you want a more complete environment

---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
<ins>On macOS</ins>:
  1) Visit https://www.python.org/downloads/ and download the macOS installer (e.g., "macOS 64-bit universal2 installer")
  2) Double-click the `.pkg` file and follow the prompts
  3) After installation, open Terminal and check:
     
     `python3 --version`
     
  5) *Alternatively* 👉 You can install Python via *Homebrew* (if you already have *Homebrew* on macOS) by running:

     `brew install python3`

---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
**Install and run Jupyter Notebooks**
  1) Once **Python** is installed (whether from python.org, your Linux package manager, or Anaconda), you can install **Jupyter Notebook** as follows:

     `pip install jupyter`

     Or **Jupyter Lab**, the next-generation web-based interface from the Jupyter project (which I'll be using):

     `pip install jupyterlab`

     (Use `pip3` if needed, e.g., › `pip3 install jupyter`) • If you install *Anaconda*, **Jupyter Notebook** is already included, so you can skip this step
  2) When everything is installed, you can start a **Jupyter Notebook** server (or**Jupyter Lab**) and work on your Python exercises by simply running in your terminal or command prompt:

     `jupyter notebook`

     or

     `jupyter lab`

     This will open a new tab in your web browser with the **Jupyter Notebook** or **Jupyter Lab** interface, ready for you to start coding!

---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "skip"} -->
\[Optional\] **Using conda:**

Setting up a conda environment for this document

```
conda create -n python_intermediate -c conda-forge jupyter jupyterlab
```

then start normally via local JupyterLab by calling `jupyter lab`

----
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "skip"} -->
\[Optional\] **Converting the Jupyter notebook to pdf:**

Run cells you want to run

Be sure to save

Call `jupyter nbconvert --to slides --post serve ./Intermediate_full.ipynb`

Go to [](http://localhost:8888/Intermediate_full.slides.html?print-pdf#/

Print via Print to PDF function of your browser
<!-- #endregion -->

<!-- #region editable=false jp-MarkdownHeadingCollapsed=true slideshow={"slide_type": "skip"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
# <ins>Table of Contents</ins>
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
  - [0. Introduction](#0.-Introduction)
    - [Set up your Python environment](#Set-up-your-Python-environment)
    - [Course objectives](#Course-objectives)
    - [Useful resources](#Useful-resources)
- [Part I](#Part-I)
  - [1. Recap](#1.-Recap)
  - [2. Data structures](#2.-Data-structures)
  - [3. Advanced string manipulation](#3.-Advanced-string-manipulation)
- [Part II](#Part-II)
  - [4. Pythonic concepts](#4.-Pythonic-concepts)
  - [5. Introduction to modules](#5.-Introduction-to-modules)
  - [6. Brief introduction to classes](#6.-Brief-introduction-to-classes)
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
# <ins>0.</ins> Introduction
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## Course objectives
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
By the end of this course, you should know:

- How to write more efficient and _Pythonic_ code using advanced language features.
- How to simplify your code with _comprehensions_ and _conditional expressions_.
- How to create flexible functions with _variable length_ argument list (`*args` and `**kwargs` magic variables).
- How to write and utilize _lambdas_ (anonymous functions).
- How to perform advanced _string manipulation_ techniques.
- How to import and use _modules_ to extend your programs.
- How to work with various data structures and understand the concept of _immutability_.
- How to create and use basic _classes_ to implement object-oriented programming principles.
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## Useful resources
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
There are plenty of resources to learn Python in the Internet from. These can be recommended by this tutorial for further learning:

- [The Python Tutorial](https://docs.python.org/3/tutorial/) from Python documentation
- [Python Cheat Sheets](https://pythononeliners.com/)
- [Collection of free Python books](https://blog.finxter.com/free-python-books/)
- [Python tips](https://book.pythontips.com/en/latest/index.html)
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
# <ins>**Part I**</ins>
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
# <ins>**1.**</ins> Recap
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
This section is a brief recap of materials covered in the Beginner Python course:

* Data Types, variables, operators
* Comments
* User input
* Reading and Writing Files
* Lists
* Repetitions and Conditions
* Functions

<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## Data Types, variables, operators
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
As with any programming language, Python can deal with many different data types. Among the basic ones are `str` strings, `int` integers, `float` floating-point numbers and `bool` booleans.

* an example of a _numeric_ value, _integer_ value;
* an integer _expression_, a basic building block of a Python _statement_;
* normal arithmetic addition
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
#### <u>Numerical</u>
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
Floating-point representation:
* A built-in `float` is typically a double-precision (64-bit) floating-point number, following the IEEE 754 standard

| Title | Storage | Smallest Magnitude | Largest Magnitude | Minimum Precision |
|-------|---------|--------------------|-------------------|-------------------|
| float | 64 bits | 2.22507 × 10e−308  | 1.79769 × 10+308  | ~15-17 digits     |
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
import sys
print(sys.float_info)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
Integer representation:
* No Fixed Bounds. You can store extremely large positive or negative integers, constrained only by the available memory
* No explicit smallest or largest representable `int`
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
import sys
print(sys.int_info)
```

```python editable=true slideshow={"slide_type": ""}
n = 1 + 2 + 4 + 10 - 3 * 6
print(n)
```

```python editable=true slideshow={"slide_type": ""}
type(n) # integer
```

```python editable=true slideshow={"slide_type": ""}
pi = 3.14159
print("Pi =", pi)
```

```python editable=true slideshow={"slide_type": ""}
type(pi) # float
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
_NOTE_: Scientific notation is supported!
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
avogadros_number = 6.022e23
c = 2.998e8
print("Avogadro's number =", avogadros_number)
print("Speed of light =", c)
```

<!-- #region editable=false jp-MarkdownHeadingCollapsed=true slideshow={"slide_type": "fragment"} -->
Used to store numbers, usually either integers, or floating point numbers.
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
#### <u>Boolean</u>
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
b1 = False
b2 = True
b = b1 and b2
print(b)
```

```python editable=true slideshow={"slide_type": ""}
type(True) # boolean
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
#### <u>String</u>
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
A string is a series of characters enclosed in quotes, either single or double, used to represent text.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
s = 'Hello, World!'
s = "Hello, " + "World!"
print(s)
```

```python editable=true slideshow={"slide_type": ""}
type(s) # string
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
Holds the value of a data type in memory!

**NOTE:** Please give variables clear and explanative names.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
enrolled_students = 728
```

```python editable=true slideshow={"slide_type": ""}
work_hours = 7.5
```

```python editable=true slideshow={"slide_type": ""}
is_loaded = False
```

```python editable=true slideshow={"slide_type": ""}
welcome_message = "Welcome!"
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
**NOTE:** Values can be overwritten!

If we define a new `welcome_message`, it changes.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
welcome_message = "Welcome, User"
```

```python editable=true slideshow={"slide_type": ""}
print(welcome_message)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
New values can be obtained by applying operators to old values, for example, mathematical operators on numerical data types `int` or `float`.
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
<u>**String Concatenation**</u>  

We can combine strings together.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
# String concatenation
hello_world = "Hello," + " World!"
print(hello_world)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
<u>**Logical Operators**</u>  
We can also determine conditions based on Boolean logic: `and`, `or`, `not`
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
**AND:**
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
a = True
b = False

if a and b:
    print("Both True!")
else:
    print("At least one False!")
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
**OR:**
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
a = True
b = False

if a or b:
    print("At least one True!")
else:
    print("Both False!")
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
**NOT:**
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
a = True

if not a:
    print("It is False!")  # If a is false
else:
    print("It is True!")
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
<u>**Numerical Operators**</u>  

- Numerical data: `+`, `-`, `*`, `/`, `%`, `**`, built-in functions `abs`, ...
- Order of execution:
    1. `()`
    2. `**`
    3. `*`, `/`
    4. `+`, `-`
    5. Left-to-right (except exponentiation!)

So, use parenthesis to make sure!
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
print("Addition:", 1 + 2)
```

```python editable=true slideshow={"slide_type": ""}
print("Subtraction:", 1 - 2)
```

```python editable=true slideshow={"slide_type": ""}
print("Multiplication:", 5 * 10)
```

```python editable=true slideshow={"slide_type": ""}
print("Division:", 10 / 5)
```

```python editable=true slideshow={"slide_type": ""}
print("Modulus:", 10 % 3)
```

```python editable=true slideshow={"slide_type": ""}
print("Exponentiation:", 2 ** 3)
```

<!-- #region editable=true slideshow={"slide_type": ""} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## Comments
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
Used to write notes or comments about code, as well as description of what the code is doing, or the variables used.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
# A single-line comment!
welcome_message = "Welcome, User!"
print(welcome_message)  # Print welcome message
```

```python editable=true slideshow={"slide_type": ""}
'''
A multi-line comment!
'''
```

```python editable=true slideshow={"slide_type": ""}
"""
Another multi-line comment!
"""
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## User Input
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
You can use `input()` to read user input: 
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
inputted_variable = float(input())
print(inputted_variable)  # Print what we just input!
type(inputted_variable)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## Reading and Writing Files
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
<u>**Opening a File**</u>

Two things to note here:
 - My object `my_file` is different from my file `"testfile.txt"`!
 - There are different modes:
     - read: `'r'`
     - (over-)write: `'w'`
     - append: `'a'`
     - read+write: `'w+'` or `'r+'`

[Python Documentation (mode)](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
# Opening and reading a file
text_file = open('data_file.txt', 'r')
content = text_file.read()
print(content)
text_file.close()
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
_NOTE_: Ensure closure of the file object when working with files in this way, or changes may not be written.
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
We can use the context manager (`with`) to allow us to simplify setup and closure of the file.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
# Using a with statement
with open('data_file.txt', 'r') as text_file:
    content = text_file.read()
    print(content)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
<u>**Reading from a File**</u>

Here are some file functions for reading from a file:

* file.read() - Read the entire file content line-by-line
* file.readlines() - Read all lines into a List object
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
with open("data_file.txt") as text_file:
    print(text_file.read())
```

```python editable=true slideshow={"slide_type": ""}
with open("data_file.txt") as text_file:
    print(text_file.readlines())
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
<u>**Writing to a File**</u>
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
One way we can write to files is using the `write()` function.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
text_file = open("testfile.txt", "w")
text_file.write("Some words \n")
text_file.write(str(25))
text_file.close()
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
Using the `with` keyword:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
with open("testfile.txt", "w") as text_file:
    text_file.write("Some words \n")
    text_file.write(str(25))
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## Lists
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
Python can work not only with basic data types mentioned before, but also with compound ones. Compound data types in Python are a powerful tool for organizing and storing data. Among the most commonly used is _lists_ which we learned about in the beginner's course.

* [List](https://docs.python.org/3/tutorial/datastructures.html#Lists)

We'll learn about other data structures later today.
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
An ordered list of items, accessed by a numerical index (starting at `0`). Elements within a list can be removed, modified, or accessed by their index, and a list can have values added to it.

Defined using square brackets `[]`.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
odd_list = [1, 3, 5, 7, 9]  # A list of odd numbers
print(odd_list)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
<u>**List Access**</u>  
You can access a list using its index value, starting from `0`.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
odd_list[0]
```

```python editable=true slideshow={"slide_type": ""}
odd_list[1]
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
_NOTE_: You can access lists in reverse index order, where `-1` is the final index. 
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
odd_list[-1]
```

```python editable=true slideshow={"slide_type": ""}
odd_list[-2]
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
<u>**Slicing**</u>   
You can also use slicing for specific partial list access.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
odd_list[1:4] # Slicing from index 1 (inclusive), to 4 (exclusive)
```

```python editable=true slideshow={"slide_type": ""}
odd_list[3:]  # Slicing from index 3 to end.
```

```python editable=true slideshow={"slide_type": ""}
odd_list[:3]  # Slicing from beginning to index 3
```

```python editable=true slideshow={"slide_type": ""}
odd_list[::2]  # Slicing with a step of 2
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
<u>**Empty List**</u>   
You can create empty lists:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
new_list = []  # An empty list
print(new_list)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## Repetitions and Conditions
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
<u>**Conditions**</u>  
In order to control program flow, and whether or not code is executed, we can do conditions based on variable values.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
x = 5

if x > 2:  # If x is GREATER THAN 2
    print("x =", x, "is GREATER THAN 2")

if x == 3:  # If x is EQUAL TO 3
    print("x =", x, "is EQUAL TO 3")

if x >= 3:  # If x is GREATER THAN or EQUAL TO 3
    print("x =", x, "is GREATER THAN or EQUAL TO 3")

if x != 0:  # If x IS NOT 0
    print("x =", x, "IS NOT 0")

if x < 4:  # If X is LESS THAN 4
    print("x =", x, "is LESS THAN 4")
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
<u>**Else/Elif**</u>  

We may also specify either/or with `if/else`, and even add extra conditions with `elif`.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
x = 10

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
<u>**Repetitions**</u>  
There are a number of ways for us to repeat lines or blocks of code within our program, to do this we use `loops`:
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
<u>For Each Loop:</u>  
A for each loop will execute its code for each item specified within the loop definition
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
animal_list = ["Cat", "Dog", "Bird"]

for animal in animal_list:
    print("Current animal is:", animal)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
The above describes `for each animal in animal_list`.
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
We are able to use a range-based for loop:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
for i in range(0, 5):
    print(i * 2) # Here we are manipulating the value each time!
```

```python editable=true slideshow={"slide_type": ""}
for i in range(0, 10, 2):  # Here we define a step of 2!
    print(i)
```

```python editable=true slideshow={"slide_type": ""}
for i in range(10, 0, -1):  # Counting down from 10, in steps of 1
    print(i)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
<u>While Loop</u>  
A `while` loop will continue until the defined condition has been met, which can potentially not happen and cause an infinite loop.

Here we are printing `n`, then incrementing it by 1, while `n` is LESS THAN 10.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
n = 0

while n < 10:
    print(n)
    n += 1
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
_NOTE_: The `break` keyword can be used to stop execution of a loop.  
_NOTE_: Use `ctrl+C` to break execution in your terminal if needed.
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": "slide"} -->
## Functions
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
A function is a reusable block of code used to perform a specific task.

We define a function using the `def` keyword, then parenthesis, which may contain the function `parameters` or `arguments` (different terms, same thing).

_NOTE_: You should give your functions and arguments explanative names.
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
<u>**Parameters/Arguments**</u>  
A function can receive 0 or more variables as arguments which are 'passed' through and are used during the execution of the function as required.
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
<u>**Returns**</u>  
A function may return a single variable, or variables, it may also return nothing where it is required to just execute some logic.
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
Here is a very basic example of a function:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
def sum_numbers(val_one, val_two):
    """Sums and returns two numbers"""
    return val_one + val_two  # Sum of both numbers

calculated_value = sum_numbers(1, 1)
print(calculated_value)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
Note that we are able to save the result of `sum_numbers`, to a variable which we have aptly named `calculated_value`, which can be reused later.
<!-- #endregion -->

<!-- #region slideshow={"slide_type": "fragment"} -->
---
Here we are modifying setting a default value for our `name` argument:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
def generate_greeting(name='Guest'):
    """
    Generate the default greeting message.
    Name will default to 'guest'.
    """
    print(f"Hello, {name}!")

generate_greeting()
generate_greeting("User")
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
Without specifying the `name` argument, the `generate_greeting` will use the default value specified within the function definition.
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
# <ins>2.</ins> Data structures
In the _Beginner_ level course, we've introduced to _lists_, the most commonly used compound data structure in Python. Here, we'll learn about methods for lists and we'll introduce to other data structures: _**dictionaries**_, _**sets**_ and _**tuples**_.

You can learn more about data structures in Python here: : [Python Documentation(Data Structures)](https://docs.python.org/3/tutorial/datastructures.html)
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
## List methods
There is a number of useful methods that can be applied to lists, let use this one as example
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
lst = [33, 84, 11]
print(lst)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
We can access the number of elements with `len`
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
print(len(lst))
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
### Adding and removing values
We can add an element with `insert` and `append`. Notice that this in the grand scheme of things this is slow, so if you can avoid this, you should:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
# add a value
lst.insert(3, 112)
print(lst)
```

```python editable=true slideshow={"slide_type": ""}
# add a value at the end
lst.append(53)
print(lst)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
removing a specific element
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
# remove the value 11
lst.remove(11)
print(lst)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
### Iterating over lists
with the `for ... in` construct we can iterate over each element of a list
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
# print the values in a list with a for loop
for i in lst:
    print(i)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
we can iterate over the list starting from the back using `reversed`
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
for i in reversed(lst):
    print(i)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
and `sorted`, sorts the values
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
for i in sorted(lst):
    print(i)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
If you want a reversed new list you need to convert the iterator into a list
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
# print the iterator
print(reversed(lst))
```

```python editable=true slideshow={"slide_type": ""}
# print the converted list
print(list(reversed(lst)))
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
### Checking if an item is in a list

with the `in` keyword you can check whether an item is in a list, with `.index(el)` you can get the index of an element
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
if 84 in lst:
    position = lst.index(84)
    print(f'84 is at index {position}')
print(lst)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
### Emptying a list
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
print(lst.clear())
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
## _Tuples_
A _tuple_ is essentially an immutable list. Indexing and slicing work the same as with lists. As with lists, you can get the length of the tuple by using the `len` function, and, like lists, tuples have `count` and `index` methods. However, since a _tuple_ is immutable, it does not have any of the other methods that lists have (such as `sort` or `reverse`). Tuples are enclosed in parentheses (`()`), though the parentheses are actually optional.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
# An empty tuple
my_tuple = tuple()
my_tuple
```

```python editable=true slideshow={"slide_type": ""}
# Initialising a tuple (different ways)
my_tuple = (1,2,3)
print(my_tuple)
my_tuple = 4,5,6
print(my_tuple)

# The way to get a tuple with one element is like this:
my_tuple = (1,)
print(my_tuple)
```

```python editable=true slideshow={"slide_type": ""}
# A practical way to exchange values between variables through tuples
a = 1
b = 2
print(a, b)
a, b = b, a
print(a, b)
```

```python editable=true slideshow={"slide_type": ""}
# Converting a list to a tuple
t1 = tuple([1,2,3])
print(t1)
```

```python editable=true slideshow={"slide_type": ""}
# Converting a string to a tuple
t2 = tuple( 'abcde ')
print(t2)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
The dictionary method `items` returns a list of tuples (see an exercise after _dictionaries_).
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
## _Sets_
A _set_ is unordered collection of unique elements, representing a mathematical set. Pythoh stores the data in a set in whatever order it wants to, so indexing has no meaning for sets unlike for lists. It looks like a list, but with no repeats, and is denoted by curly braces (`{}`).
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
# An empty set
my_set = set()
my_set
```

```python editable=true slideshow={"slide_type": ""}
# Initialising a set
my_set = {1, 2, 3, 4, 5}
my_set
```

```python editable=true slideshow={"slide_type": ""}
# Converting a list to a set
set([1,4,4,4,5,1,2,1,3])
```

```python editable=true slideshow={"slide_type": ""}
# Converting a string to a set
set('this is a string')
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
There are a few operators that work with sets as well as some useful methods:

| Operator | Description          | Example                        |
|----------|----------------------|--------------------------------|
| `\|`     | union                | `{1,2,3} \| {3,4} → {1,2,3,4}` |
| `&`      | intersection         | `{1,2,3} & {3,4} → {3}`        |
| `-`      | difference           | `{1,2,3} - {3,4} → {1,2}`      |
| `^`      | symmetric difference | `{1,2,3} ^ {3,4} → {1,2,4}`    |
| `in`     | is an element of     | `3 in {1,2,3} → True`          |

| Method            | Description                                   |
|-------------------|-----------------------------------------------|
| `S.add(x)`        | Add `x` to the set                            |
| `S.remove(x)`     | Remove `x` from the set                       |
| `S.issubset(A)`   | Returns `True` if S ⊂ A and `False` otherwise |
| `S.issuperset(A)` | Returns `True` if A ⊂ S and `False` otherwise |

There are also _set comprehensions_ just like list comprehensions.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
s = {i**2 for i in range(12)}
print(s)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
### _Example 1_
Removing repeated elements from lists
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
L = [1,4,4,4,5,1,2,1,3]
L = list(set(L))
print(L)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
### _Example 2_
Wordplay: an example of an `if` statement that uses a `set` to see if every letter in a
word is either an `a`, `b`, `c`, `d`, or `e`:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
word = "bed"

if set(word).issubset("abcde"):
    print(f"All letters in '{word}' are within 'abcde'.")
else:
    print(f"'{word}' contains letters outside of 'abcde'.")
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
## _Dictionaries_
A _dictionary_ is an unordered collection of key-value pairs, representing flexible mapping of keys to values. It's like a more general version of a list. In other words, it's an associative container permitting access based on a key, not an index. Dictionary items are colon-connected (`:`) key-value pairs enclosed by curly braces (`{}`).
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": null} -->
- _Dictionaries_ are like labelled drawers:
  - the label of the drawer is called a key;
  - however dictionaries are "kind of" unordered;
  - the content of that drawer is called the value;
  - like lists, the types of keys and values do not have to match;
  - keys need to be "hashable", usually basic data types.

The syntax is `{'key': value}` or `dict(key=value)`.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
# An empty dictionary
my_dict = {}
my_dict
```

```python editable=true slideshow={"slide_type": ""}
# Another empty dictionary
my_dict = dict()
my_dict
```

```python editable=true slideshow={"slide_type": ""}
# Initialising a dictionary
my_dict = {
    'temperature_k': 298.5,
    'pressure': 1.015
}
my_dict
```

```python editable=true slideshow={"slide_type": ""}
# Another way to initialise a dictionary
my_dict = dict(temperature_k=298.5, pressure=1.015)
my_dict
```

```python editable=true slideshow={"slide_type": ""}
# Add a new key-value pair to the dictionary
my_dict['volume'] = 100.0
my_dict
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
### _Example_
Extending a list to a dictionary
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
# A list containing the number of days in the months of the year
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
```

```python editable=true slideshow={"slide_type": ""}
# How many days in January and in June? Not the best idea to store this data in lists
print(f"In January, there are {days[0]} days")
print(f"In June, there are {days[5]} days")
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
## Notes on _lists_, _strings_, _tuples_, _sets_, and  _dictionaries_
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
* **_Lists_** and **_dictionaries_** are _mutable_, which means their contents can be changed.
* **_Strings_** and **_tuples_** are _immutable_, which means they cannot be changed.
* **_Lists_** are typically for homogeneous data sequences (ingredients, names) whereas **_tuples_** are ideal for heterogeneous data (entries with different meanings).
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
Similarities of _lists_ and _strings_:
* `len` function: the number of items in a list/string
* `in` operator: tells if a list/string contains something
* `+` and `*` operators: concatenating and repeating
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
[7, 8] + [3, 4, 5]
```

```python editable=true slideshow={"slide_type": ""}
[0] * 5
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
* _Indexing_: simple to "grab" an item/character in a list/string if you know where it sits
* _Slicing_: use `:` to "grab" a range defined subsection of a list/string:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
a_lst = ['a','b','c','d','e','f','g','h','i','j']
print(a_lst[4])
a_str = "abcdefghij"
print(a_str[4])
start=3
stop=7
# items start to stop-1
print(a_lst[start:stop])
print(a_str[start:stop])
# items start to the end of list/string
print(a_lst[start:])
print(a_str[start:])
# items from beginning of list/string to stop-1
print(a_lst[:stop])
print(a_str[:stop])
# whole list/string
print(a_lst[:])
print(a_str[:])
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
* _Looping_:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
for i in range(len(a_lst)):
    print(a_lst[i])
```
```python editable=true slideshow={"slide_type": ""}
for item in a_lst:
    print(item)
```
```python editable=true slideshow={"slide_type": ""}
for i in range(len(a_str)):
    print(a_str[i])
```
```python editable=true slideshow={"slide_type": ""}
for item in a_str:
    print(item)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
_Lists_ and _strings_ behave differently when we try to make copies.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
s = 'Hello '
copy = s
s = s + '!!! '
print( 's is now: ', s, '; Copy: ', copy)
```

```python editable=true slideshow={"slide_type": ""}
L = [1,2,3]
copy = L
L[0] = 9
print( 'L is now: ', L, 'Copy: ', copy)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
Everything in Python is an object. This includes numbers, strings, and lists and any other data structure. When we
do a simple assignment for a scalar _variable_, like `x=487`, the variable `x` acts as a _reference_ to that object. All objects are treated the same way. In the example of a _string_ above, `copy` is another reference to `'Hello'`. When we do `s=s+'!!!'`, `s` is now referencing another new string object because strings are _immutable_. Whereas in the example of a _list_, when we change an element in the list, no new list is created, the old list is actually changed _in place_ because lists are _mutable_.

So, how to modify the example with a list, so that it behaves as expected? We need to create a new copy of the entire list, which is done by `L[:]`
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
L = [1,2,3]
copy = L[:]
L[0] = 9
print( 'L is now: ', L, 'Copy: ', copy)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## Have a Play!
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
### _Exercise 1 (dictionaries)_
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
1) Create a dictionary of the days in the months of the year.
2) Print out the number of the days for any month as it was done for lists.
<!-- #endregion -->


<!-- #solution -->
```python editable=true slideshow={"slide_type": ""}
# Create the dictionary with months as keys and days as values
months_days = {
    "January": 31,
    "February": 28,  # ignoring leap years for simplicity
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

# Ask the user for a month
month_input = input("Enter the name of a month (e.g., 'January'): ")

# Print the number of days for the entered month
if month_input in months_days:
    print(f"{month_input} has {months_days[month_input]} days.")
else:
    print("That doesn't seem to be a valid month name.")

```
<!-- #endsolution -->

<!-- #region editable=true slideshow={"slide_type": ""} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
### _Exercise 2 (dictionaries)_
<!-- #endregion -->

<!-- #region editable=false jp-MarkdownHeadingCollapsed=true slideshow={"slide_type": ""} -->
1. Create a dictionary of several countries and capitals. Think about what's going to be a key and a value.
2. Try create the initial dictionary by initialising it.
   Try to add new countries with their capitals.
3. Print out the whole dictionary line by line in a loop each representing a country and its capital respectfully.
<!-- #endregion -->

<!-- #solution -->
```python editable=true slideshow={"slide_type": ""}
# 1) Create a dictionary of countries and their respective capitals
capitals = {
    "United States": "Washington, D.C.",
    "Germany": "Berlin",
    "France": "Paris"
}

# 2) Add new countries with their capitals
capitals["Italy"] = "Rome"
capitals["Spain"] = "Madrid"

# 3) Print out each country and its capital
for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}.")

```
<!-- #endsolution -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
### _Exercise 3 (tuples)_
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
Try `items()` method on the dictionary you've created before. Print that out. What kind of data structure does it return?
<!-- #endregion -->

<!-- #solution -->
```python editable=true slideshow={"slide_type": ""}
# Get the items() of the dictionary
items_result = capitals.items()

# Print the result
print("Items:", items_result)

# Print the type of the returned data structure
print("Type:", type(items_result))

```
<!-- #endsolution -->

<!-- #region editable=false slideshow={"slide_type": "notes"} -->
_Note_: the data structure returned by `dict.items()` is of type `dict_items`,
which is an iterable view object displaying the dictionary’s (key, value) pairs
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
### _Exercise 4 (lists)_
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
Given this list: 
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
numbers = [42, 15, 7, 29, 89, 15]
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
Complete these tasks:
<!-- #endregion -->

<!-- #solution -->
```python editable=true slideshow={"slide_type": ""}
# 1. Print all numbers in reverse order using reversed()
# Expected output: 15 89 29 7 15 42
for num in reversed(numbers):
    print(num, end=' ')

# 2. Create a new sorted list called 'sorted_numbers' without modifying the original
# Expected output: [7, 15, 15, 29, 42, 89]
sorted_numbers = sorted(numbers)

# 3. Check if 29 is in the list. If it is, print its index position
# Expected output: "29 is at index 3"
if 29 in numbers:
    print(f"29 is at index {numbers.index(29)}")

```
<!-- #endsolution -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
# <ins>3.</ins> Advanced string manipulation
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
* Adjusting case
* Formatting strings
  - _Note_: Modification requires assignment, because these functions return a copy, not modifying the original string
* `find()` and `index()`: return index of a substring, but the latter raises a `ValueError` exception when not found (_exception handling_)
* Quering the existence, replacing, splitting
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
line = "the quick brown fox jumped over a lazy dog"
print(line.find('fox'))
print(line.startswith('the'))
print(line.endswith('fox'))
print(line.replace('brown', 'red'))
print(line.split())
try:
    index = line.index('bear')
    print(index)
except ValueError:
    print("A bear isn't mentioned in the text")
```

```python editable=true slideshow={"slide_type": ""}
arc_update = "ThE HAmILton suPERcompUTER is beiNg UPGraded"
print(arc_update.upper())
print(arc_update.title())
print(arc_update.capitalize())
print(arc_update)
arc_update = "   RSE   "
print(arc_update.strip())
print(arc_update.rstrip())
print(arc_update.lstrip())
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
* The canonical way to search a string (if not interested in the index) is very simple:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
line = "the quick brown fox jumped over a lazy dog"
if "fox" in line:
    print("A fox has been seen")
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
* _F-strings_ provide a way to embed expressions inside string literals, using a minimal syntax
  - expressions are evaluated at runtime and replaced with their values
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
interests = ["football", "zoom"]
print(f"Bob enjoys {interests[0]} and {interests[1]}")

weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
for weekday in weekdays:
    print(f"Today is {weekday}")

age = 70
print(f"Soon I'll be {age+1}!")
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false jp-MarkdownHeadingCollapsed=true slideshow={"slide_type": "slide"} -->
# <ins>**Part II**</ins>
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
# <ins>4.</ins> Pythonic concepts
* _Comprehensions_
* _Conditional expressions_
* Advanced function arguments
* How control flow are actually implemented - _iterators_
* _Lambdas_ - anonymous functions
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## _Comprehensions_
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
### `list` comprehensions
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
Multiples of three:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
multiples_of_three = [i for i in range(20) if i%3 == 0]
print(multiples_of_three)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
For instance you would usually do something like this:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
squared = []
for x in range(10):
    squared.append(x**2)
print(squared)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
You can simplify it using list comprehensions:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
squared = [x**2 for x in range(10)]
print(squared)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
### `dict` comprehensions
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}
print(mcase_frequency)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
### `set` comprehensions
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
squared = {x**2 for x in [1, 1, 2]}
print(squared)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## _Conditional expressions_
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
They are known as _ternary operators_ in other languages. They became a part of Python from version 2.4
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
hungry = True
state = "grumpy" if hungry else "content"
print(state)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
Another more obscure and not widely used example involves tuples
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
nice = False
personality = ("mean", "nice")[nice]
print("The cat is", personality)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
There is also a shorter version of the normal ternary operator you have seen above (introduced in Python 2.5)
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
output = None
msg = output or "No data returned"
print(msg)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
As a simple way to define function parameters with dynamic default values
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
def my_function(real_name, optional_display_name=None):
    optional_display_name = optional_display_name or real_name
    print(optional_display_name)

my_function("John")
```

```python editable=true slideshow={"slide_type": ""}
my_function("Mike", "anonymous123")
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## _Advanced function arguments_
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
You have already learned that functions can have arguments, and these can be called as keyword arguments. 
Say we want to build a function summing up arguments, but there can be a different number of arguments:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
def sum2(arg1, arg2):
    return arg1 + arg2

def sum3(arg1, arg2, arg3):
    return arg1 + arg2 + arg3

...

print(sum2(2,3))
print(sum3(2,3,4))
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
The answer to not make it tedious is to use *args as argument.
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
### Using `*args` in a function to catch arguments
We can use `*args` to catch all non-keyword arguments as a tuple and sum over them
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
# sum_args sums over all arguments
def sum_args(*args):
    accumulator = 0
    for arg in args:
        accumulator += arg
    return accumulator

# print with the same arguments as before
print(sum_args(2,3))
print(sum_args(2,3,4))
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
### Using *args in function invocation
If we call a function with `*arguments` it will unpack them. The variable arguments will need to be iterable (such as a list or a tuple).
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
numbers = (2, 3)

# call sum2 with unpacked *var2
print("Value unpacking with sum2(*numbers):", sum2(*numbers))

# Demonstrate that this is the same as calling on the separate arguments
print("Because numbers has length 2 this is identical to sum2(numbers[0], numbers[1]):", sum2(*numbers))
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
### Using `**kwargs` in a function to catch keyword arguments
Similarly, we can catch keyword arguments as a dictionary
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
def print_kwargs(**kwargs):
    print("keywords: ", kwargs.keys())
    print("values: ", kwargs.values())

print_kwargs(first_arg=12, second_arg="super")
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
### Using `**kwargs` in command invocation
We can also assign the values of a dictionary to the names of function arguments. This really useful to assemble your values to call a function.
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
def flower_output(flower_name, colour):
    print(f'{flower_name}s are {colour}')

flower_dict = {}
flower_dict['flower_name'] = 'rose'
flower_dict['colour'] = 'red'

flower_output(**flower_dict)
```

<!-- #region editable=false raw_mimetype="" slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## _Iterators_ beneath control flows
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
But what is the for loop doing under the hood?
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
1. `iter()` is called on the container object returning an iterator object
2. The iterator object defines a `__next__()` function which facilitates access to elements one at a time
3. `__next()__` tells for loop when there are no more elements raising StopIteration exception
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
uni = "Durham"
it = iter(uni)
it
```

```python editable=true slideshow={"slide_type": ""}
next(it)
```

```python
next(it)
```

```python
next(it)
```

```python
next(it)
```

```python
next(it)
```

```python
next(it)
```

```python editable=true slideshow={"slide_type": ""}
next(it)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## _Lambda_ functions
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
**_Lambda functions_** for compact inline function definitions. Useful when you don’t want to use a function twice:

`lambda arguments : manipulate(argument)`

Or more generally:

`somefunc = lambda a1, a2, ... : some_expression`
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
add = lambda x, y: x + y
print(add(3, 5))
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
_Example_: List sorting
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print(a)
```

<!-- #region editable=true slideshow={"slide_type": "fragment"} -->
---
_Example_: Parallel sorting of lists
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
list1 = ["New York", "Moscow", "Tokyo"]
list2 = [8804190, 13010112, 14187176]
data = zip(list1, list2)
print(data)
data = sorted(data)
print(data)
list1, list2 = map(lambda t: list(t), zip(*data))
print(list1)
print(list2)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
**_Map_** applies a function to all the items in an iterable:

`map(function_to_apply, list_of_inputs)`
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
items = [1,2,3,4,5]
squared = []
for i in items:
    squared.append(i**2)
print(squared)
```

```python editable=true slideshow={"slide_type": ""}
squared = list(map(lambda x: x**3, items))
print(squared)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## Have a play!

#### List Comprehension Basics
Create a list of even numbers between 1 and 20 using a list comprehension.

Hint Remember the `range()` function and modulo operator `%`
<!-- #endregion -->

<!-- #solution -->
```python editable=true slideshow={"slide_type": ""}
# Uncomment below and continue with your solution:
#even_numbers =
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
even_numbers

```
<!-- #endsolution -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
#### Dictionary Comprehension
Given this dictionary of fruits and their quantities, create a now dictionary where the number of fruits are doubled
<!-- #endregion -->

<!-- #solution -->
```python editable=true slideshow={"slide_type": ""}
# Uncomment below and continue with your solution:
#fruits = {'apple': 5, 'banana': 3, 'orange': 2, 'pear': 1}
fruits = {'apple': 5, 'banana': 3, 'orange': 2, 'pear': 1}
doubled_fruits = {fruit: amount * 2 for fruit, amount in fruits.items()}
doubled_fruits

```
<!-- #endsolution -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
#### Conditional Expression
Write a function that takes a number and returns 'positive' if > 0, 'negative' if < 0, and 'zero' if 0, using a conditional expression.
<!-- #endregion -->

<!-- #solution -->
```python editable=true slideshow={"slide_type": ""}
# Uncomment below and continue with your solution:
#def check_number(num):
#    return # Your code here
def check_number(num):
    return 'positive' if num > 0 else 'negative' if num < 0 else 'zero'
check_number(5)

```
<!-- #endsolution -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
#### Args Practice
Write a function that takes any number of strings and returns them concatenated with spaces between them.

Hint: Think about `join()` and how it works with strings
<!-- #endregion -->

<!-- #solution -->
```python editable=true slideshow={"slide_type": ""}
# Example: combine_strings('hello', 'world') returns 'hello world'
# Uncomment below and continue with your solution:
#def combine_strings(*args):
#    return # Your code here
def combine_strings(*args):
    return ' '.join(args)

combine_strings('hello', 'world')

```
<!-- #endsolution -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
#### Lambda and Sorting
Sort this list of dictionaries by the 'age' key using a lambda function.

Hint: The `sort`/`sorted` function takes a key parameter
<!-- #endregion -->

<!-- #solution -->
```python editable=true slideshow={"slide_type": ""}
# Continue with your solution below:
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 20},
    {'name': 'Charlie', 'age': 30}
]
#sorted_people = # Your code here
sorted_people = sorted(people, key=lambda x: x['age'])
sorted_people

```
<!-- #endsolution -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
# <ins>5.</ins> Introduction to modules
A _module_ is a single file (or collection of files) that is intended to be imported and used in other Python programs. It can include functions, classes, variables, and runnable code.
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## Importing _modules_
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
Python comes with hundreds of _modules_ doing all sorts of things. Also, many 3rd-party modules are available to download from the Internet.
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
There are several ways of importing _modules_:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
# import the whole module
import math

# module's function name is in the module's namespace
print(math.sqrt(16.0))
```

```python editable=true slideshow={"slide_type": ""}
# import several modules at once
import os, sys, time
```

```python editable=true slideshow={"slide_type": ""}
# use 'as' keyword to change the name of the module
import math as m
print(m.sqrt(36.0))
```

```python editable=true slideshow={"slide_type": ""}
# import only a selected function from a module
from math import sqrt

# the function's name is in the global namespace
print(sqrt(49))
```

```python editable=true slideshow={"slide_type": ""}
# change the name of the function in the module
from math import sqrt as square_root
print(square_root(25))
```

```python editable=true slideshow={"slide_type": ""}
# import all functions, variables, and classes from a module into the global namespace
# - better to avoid this as some names from the module can interfere with your own variable names in the global namespace
from math import *
print(int(sqrt(4.0)))
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
To get help on a module at the Python shell, import it the whole (the very first way), then you can...
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
# get a list of the functions and variables in the module
dir(math)
```

```python editable=true slideshow={"slide_type": ""}
# get a long description
help(math)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## Some useful _modules_
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
Python comes with a program called pip which will automatically fetch packages released and listed on PyPI: `pip install <some-module>`
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
| Name       | Description |
|------------------|-------------|
| **`time`**       | functions for dealing with time
| **`datetime`**   | allows to work with dates and times together
| **`os`**         | functions for working with files, directories and operating system
| **`shutils`**    | contains a function to copy files
| **`sys`**        | contains a function to quit your program
| **`zipfile`**    | allows to compress/extract files or directory of files into/from a zip file
| **`urllib`**     | allows to get files from the internet
| **`math`**       | math functions such as `sin`, `cos`, `tan`, `exp`, `log`, `sqrt`, `floor`, `ceil` |
| **`numpy`**      | fundamental package for scientific computing (a multidimensional array object; routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting; basic linear algebra, basic statistical operations, random simulation and much more) |
| **`scipy`**      | a collection of mathematical algorithms and convenience functions built on the NumPy extension (high-level commands and classes for the manipulation and visualization of data) |
| **`matplotlib`** | library for plotting
| **`sympy`**      | symbolic computations
| **`itertools`**  | provides a generator-like object named `permutations`
| **`csv`**        | parsing and writing `csv` files
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## Using _modules_
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
### _Example_
Interfacing with the operating system: **`os`**
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
import os
home = "/home"
print(os.path.join(home, os.environ["USER"], "holiday_planning.txt"))
print(os.listdir("/home/dmitry/Desktop"))
if not os.path.exists("nofile.txt"):
    print("File not found")
    exit(1)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
We'll demonstrate how to use modules in the actual code using the example of reading/writing files. In the _Beginner_ course, we showed the basic reading/writing files using the built-in functions of Python. But there's a better way of doing that by means of the specialised module called **`csv`**.
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
Writing a csv file:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
import csv, math

with open ("example.csv", 'w') as out_f:
    writer = csv.writer(out_f, delimiter=',')
    writer.writerow(["x_axis", "y_axis"])
    x_axis = [x * 0.1 for x in range(0, 100)]
    for x in x_axis:
        writer.writerow([x, math.cos(x)])
```

<!-- #region editable=false jp-MarkdownHeadingCollapsed=true slideshow={"slide_type": "fragment"} -->
---
Now, let’s extract the value for `y_axis` when `x_axis` is `1.0` for the csv we just wrote:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
import csv

with open ("example.csv", 'r') as in_f:
    reader = csv.reader(in_f, delimiter=',')
    next(reader) # skip header
    for row in reader:
        if row[0] == "1.0":
            print(row[1])
            break
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## Building your own module

  - If you have a .py file in a path that is available to python, you can import any object defined in that file.
  - If you have `mymodule.py` in your folder you can just write:
    `import mymodule`
    and use a function defined in there with `mymodule.my_function(arg)`
  - of course you can also use the  method
    `from mymodule import my_function`
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
### ```__main__``` special built-in variable
So python files can be executed with 
`python mymodule.py` or loaded from with `import`
However, all commands just put into a python file will be executed on import.

The answer is to introduce a `__main__` block that is only executed when the file is called as a script.
It is good practice to have all code executed in a script to be either in a function or in this block.

<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->

### Example content of `mymodule.py`:
```python
def myfunction():
    print("I will be only printed when the function is called")

print("I will be called on import and execution as a script")

if __name__ == "__main__":
    print("I will only executed when called as a script")
```
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## Have a play!

 - (1) Try to put the example content from the last slide into a `mymodule.py` in your folder, (2) import `myfunction` into this notebook and (3) run it.
 - (4) Add your own function that returns the sine of a value (you might need to restart the kernel in the tab _Kernel_-> _Restart Kernel_) if you have already executed the import.
 - (5) Test it (import the module with your new function and run it).

<!-- #endregion -->

<!-- #solution -->
```python editable=true slideshow={"slide_type": ""}
# solution hint, cell 1
# (this is done with this notebook here, but usually you create this outside of python in an external editor)
# Write the content into the module file:

module_path = 'mymodule.py'

module_content = """
def myfunction():
    print("I will be only printed when the function is called")

print("I will be called on import and execution as a script")

if __name__ == "__main__":
    print("I will only executed when called as a script")
"""

with open(module_path, 'w') as fobj:
    fobj.write(module_content)

```
<!-- #endsolution -->

<!-- #solution -->
```python editable=true slideshow={"slide_type": ""}
# solution hint, cell 2
# Import the module:
import mymodule

```
<!-- #endsolution -->

<!-- #solution -->
```python editable=true slideshow={"slide_type": ""}
# solution hint, cell 3
# Call the function from the module:
mymodule.myfunction()

```
<!-- #endsolution -->

<!-- #solution -->
```python editable=true slideshow={"slide_type": ""}
# solution hint, cell 4
# To avoid the kernel restart, we output into a second file:
module_path = 'mymodule2.py'

module_content2 = """
import math

def useless_sine(value):


def myfunction():
    print("I will be only printed when the function is called")

print("I will be called on import and execution as a script")

if __name__ == "__main__":
    print("I will only executed when called as a script")
"""

with open(module_path, 'w') as fobj:
    fobj.write(module_content)

```
<!-- #endsolution -->

<!-- #solution -->
```python editable=true slideshow={"slide_type": ""}
# solution hint, cell 4
# Import your module and run the sine function from your own module:
mymodule2.useless_sine(1.57)

```
<!-- #endsolution -->


<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
# <ins>6.</ins> Brief introduction to classes
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": ""} -->
* Python is an object oriented programming language. Object-Oriented Programming is a programming paradigm based on the concept of "objects" which can contain:
  - Data (attributes)
  - Code (methods)
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
### What is OOP?
Key OOP Concepts:

1. **Classes and Objects**
   - Class: A blueprint for creating objects
   - Object: An instance of a class


A simple example:
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
# Simple example
class Dog:
    def __init__(self, name):
        self.name = name  # attribute
        
    def bark(self):      # method
        print(f"{self.name} says woof!")

# Creating objects
dog1 = Dog("Rex")
dog2 = Dog("Buddy")
dog1.bark()  # Rex says woof!
```

- `__init__`: The constructor method to initialize the attributes.

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
2. **Encapsulation**
   - Bundling data and methods that work on that data within one unit
   - Restricting access to certain details
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
class BankAccount:
    def __init__(self):
        self._balance = 0  # protected attribute
        
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            
    def get_balance(self):
        return self._balance
```

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
3. **Inheritance**
   - Creating new classes that are built upon existing classes
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"
```

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
4. **Polymorphism**
   - Different classes can be treated through the same interface
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
def make_speak(animal):
    print(animal.speak())

cat = Cat("Whiskers")
make_speak(cat)  # Whiskers says meow!
```

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
"Real-World" Example: The Elephant and Refrigerator

How do you put an elephant into a refrigerator? Old style (without classes):
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
# define elephant size
elephant_x = 5
elephant_y = 5
elephamt_h = 5

# define refrigerator size
refrigerator_x = 6
refrigerator_y = 6
refrigerator_h = 6

def open_refrigerator_door():
    print('Refrigerator door is opened')

def package_elephant():
    print('Elephant is packaged')

def put_elephant_to_refrigerator():
    print('Elephant is in the fridge already')

def close_refrigerator_door():
    print('Close the refrigerator door')

# compare size
if elephant_x < refrigerator_x and elephant_y < refrigerator_y and elephamt_h < refrigerator_h:
   open_refrigerator_door()
   package_elephant()
   put_elephant_to_refrigerator()
   close_refrigerator_door()
else:
    print('refrigerator is too small to put elephant')
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
Now let's look at our elephant and refrigerator example through OOP principles:

1. **Encapsulation**: Both `Elephant` and `Refrigerator` classes keep their properties (dimensions) and behaviors (package, open_door) together
2. **Abstraction**: The complex logic of putting an elephant in a refrigerator is hidden behind simple method calls
3. **Object Interaction**: The `Refrigerator` class works with `Elephant` objects
<!-- #endregion -->

```python editable=true slideshow={"slide_type": ""}
class Elephant:
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.h = h

    def package(self):
        print('Elephant is packaged')

class Refrigerator:
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.h = h
        self.is_door_open = False

    def open_door(self):
        self.is_door_open = True
        print('Refrigerator door is opened')

    def close_door(self):
        self.is_door_open = False
        print('Close the refrigerator door')

    def put_elephant(self, elephant):
        if not self.is_door_open:
            self.open_door()
        if elephant.x < self.x and elephant.y < self.y and elephant.h < self.h:
            elephant.package()
            print('Elephant is in the fridge already')
        else:
            print('Refrigerator is too small to put elephant')
        self.close_door()

# Define element sizes
elephant_x = 5
elephant_y = 5
elephant_h = 5

# Define refrigerator sizes
refrigerator_x = 6
refrigerator_y = 6
refrigerator_h = 6

# Create instances of Elephant and Refrigerator classes
elephant = Elephant(elephant_x, elephant_y, elephant_h)
refrigerator = Refrigerator(refrigerator_x, refrigerator_y, refrigerator_h)

# Put the elephant in the refrigerator
refrigerator.put_elephant(elephant)
```

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
1. The `Elephant` class contains the `package` method.

2. The `Refrigerator` class contains methods for opening and closing the door (`open_door` and `close_door`) 
as well as putting the elephant inside (`put_elephant`).

3. The logic to determine if the elephant fits into the refrigerator is now part of the `put_elephant` method.

4. We create instances of the `Elephant` and `Refrigerator` classes and use the `put_elephant` method to put the elephant into the refrigerator.
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
## Have a play!
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "subslide"} -->
### Exercise: Building a Car Management System 🚗

Create a `Car` class that simulates basic car operations. This exercise will help you practice working with class attributes and methods.

1. Create a `Car` class with the following features:
   - Store basic car information:
     - `make`: The make of the car (e.g., Toyota, Honda);
     - `model`: The model of the car (e.g., Camry, Civic);
     - `year`: The year the car was manufactured;
     - `color`: The color of the car;
     - `mileage`: The current mileage of the car.
   - Allow the car to be driven:
     - `drive(distance)`: A method that takes a distance in miles as a parameter and increases the mileage of the car accordingly.
   - Enable car repainting:
     - `paint(new_color)`: A method that changes the color of the car;
   - Display car information:
     - `display_info()`: A method that displays all the information about the car (make, model, year, color, and mileage).
<!-- #endregion -->

<!-- #solution -->
```python editable=true slideshow={"slide_type": ""}
# Uncomment below and continue with your solution:
#class Car:
#    def __init__(...):

class Car:
    def __init__(self, make, model, year, color, mileage, num):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage
        self.num = num

    def drive(self, distance):
        self.mileage += distance

    def paint(self, new_color):
        self.color = new_color

    def re_register(self, new_num):
        self.num = new_num

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Mileage: {self.mileage}")
        print(f"plate number: {self.num}")


# Test the Car class
car1 = Car("Toyota", "Camry", 2020, "Blue", 15000, "DUR 888")
car1.display_info()

car1.drive(100)
car1.paint("Red")
car1.display_info()
################
car1.re_register('DUR 666')
car1.display_info()
```
<!-- #endsolution -->

<!-- #region editable=false slideshow={"slide_type": "fragment"} -->
---
<!-- #endregion -->

<!-- #region editable=false slideshow={"slide_type": "slide"} -->
# Thank You for Attending! 👋

- Feedback would really be appreciated (see the link in the email I've sent)
- Check out our other training courses at ARC:
  - https://www.durham.ac.uk/research/institutes-and-centres/advanced-research-computing/training-/
- RSE support by ARC at Durham University:
  - https://www.durham.ac.uk/research/institutes-and-centres/advanced-research-computing/research-software-engineering/

#### Contact
- Email: arc-rse@durham.ac.uk

Happy Coding! 🐍