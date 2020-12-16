# **Writing Command Line Interface (CLI) in python**

The command line interface (also known as CLI) is a means to interact with a command line script.

Python comes with several different libraries that allow you to write a command line interface for your scripts, but the standard way for creating a CLI in Python is currently the Python argparse library.

- An argument is a single part of a command line, delimited by blanks.

- An option is a particular type of argument (or a part of an argument) that can modify the behavior of the command line.

- A parameter is a particular type of argument that provides additional information to a single option or command.

```bash
$ ls -l -s -k /var/log
# 5 arguments = 1 cmd, 3 options, 1 parameter

$ ls -lsk /var/log
# 3 arguments = 1 cmd, 1 option (combined), parameter

```

Using the Python argparse library has four steps:

1. Import the Python argparse library
2. Create the parser
3. Add optional and positional arguments to the parser
4. Execute `.parse_args()`

The `.parse_args()` function returns a `Namespace` object that contains a simple property for each input argument received from the command line.

sample code

```python
# myls.py
# Import the argparse library
import argparse

import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(description='List the content of a folder')

# Add the arguments
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to list')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))
```

- we can set the name and description of the program using the `prog` keyword inside the `argparse.ArgumentParser()`
