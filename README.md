# TexImpRes

> User-friendly markdown and text "compiler" to use imports, variables and comments

![](docu/generation.gif)

## Table of contents
1. [How to use TexImpRess / Usage](#how-to-use-teximpres)
2. [Keywords](#keywords)
3. [Examples](#examples)

## How to use TexImpRes
To use TexImpRes pull this repository and install Python3 (version 3.10 recommended).  
Create text/markdown file/-s (for example `main.md`) that is using some [keywords](#keywords).  
With the following command you select the `main.md` as entry-file and `result.md` as "compiled" output file:
```commandline
python3 src/main.py main.md result.md
```

## Keywords

### Imports 
With import`s you can copy the content of a file and paste them at the selected position.  
Imports are used like this:  
```text
@import "the_file_you_want_to_import.txt"
```
**Example:**  
*File: main.txt*
```
1
2
3
@import "number_4_to_6.txt"
7
8
9
```
*File: number_4_to_6.txt*  
```
4
5
6
```
*If you run `python3 src/main.py main.txt output.txt` and then open `output.txt` you see this:*
```
1
2
3
4
5
6
7
8
9
```

### Variables
With variables you can dynamically add values to you files.  
You can define variables like this:
```text
@var my_name = "John Doe"
@var NUMBER_PI = "3.141592"
```
and use them like this:
```text
Hey $my_name nice to meet you!
Did you already know that pi is $NUMBER_PI?
```
**Example:**  
*File: main.txt*
```text
@import "person_1.txt"
$name ist $age years old!
@import "person_2.txt"
$name ist $age years old!
```
*File: person_1.txt*
```text
@var name = "Paul"
@var age = "19"
```
*File: person_2.txt*
```text
@var name = "Alice"
@var age = "32"
```
*If you run `python3 src/main.py main.txt output.txt` and then open `output.txt` you see this:*
```
Paul ist 19 years old!
Alice ist 32 years old!
```

### Comments
With comments you can document lines of code, these comments will later be removed from the output file!  
You can define comments like this:
```text
@comment lorem ipsum...
```
**Example:**  
*File: main.txt*
```text
Pi is 3.141592...
@comment this text will not be removed in the output file :D
@comment sure!
Did you know this fact?
```
*If you run `python3 src/main.py main.txt output.txt` and then open `output.txt` you see this:*
```
Pi is 3.141592...
Did you know this fact?
```

## Examples
You find some examples [here](examples/README.md).