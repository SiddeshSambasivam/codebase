## **Notes on PEP8 standards**

### **Imports**

Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.

Imports should be grouped in the following order:

1. Standard library imports.
2. Related third party imports.
3. Local application/library specific imports.

You should put a blank line between each group of imports.

### **Module Level Dunder Names**

Module level "dunders" (i.e. names with two leading and two trailing underscores) such as \_\_all\_\_, \_\_author**, \_\_version**, etc. should be placed after the module docstring but before any import statements except from \_\_future\_\_ imports. Python mandates that future-imports must appear in the module before any other code except docstrings:

```python
"""This is the example module.

This module does stuff.
"""

from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys

```

### **Naming Conventions**

- b (single lowercase letter)

- B (single uppercase letter)

- lowercase

- lower_case_with_underscores

- UPPERCASE

- UPPER_CASE_WITH_UNDERSCORES

- CapitalizedWords (or CapWords, or CamelCase -- so named because of the bumpy look of its letters [4]). This is also sometimes known as StudlyCaps.

  Note: When using acronyms in CapWords, capitalize all the letters of the acronym. Thus HTTPServerError is better than HttpServerError.

- mixedCase (differs from CapitalizedWords by initial lowercase character!)
  Capitalized_Words_With_Underscores (ugly!)

In addition, the following special forms using leading or trailing underscores are recognized (these can generally be combined with any case convention):

\_single_leading_underscore: weak "internal use" indicator. E.g. from M import \* **does not import objects whose names start with an underscore.**

single*trailing_underscore*: used by convention to avoid conflicts with Python keyword, e.g.

```python
tkinter.Toplevel(master, class_='ClassName')
```

**double_leading_underscore: when naming a class attribute, invokes name mangling (inside class FooBar, **boo becomes \_FooBar\_\_boo; see below).

**double_leading_and_trailing_underscore**: "magic" objects or attributes that live in user-controlled namespaces. E.g. **init**, **import** or **file**. Never invent such names; only use them as documented.

### **Misc**

- Trailing commas are usually optional, except they are mandatory when making a tuple of one element (and in Python 2 they have semantics for the print statement). For clarity, it is recommended to surround the latter in (technically redundant) parentheses:

  ```python
  # Correct:
  FILES = ('setup.cfg',)

  # Wrong:
  FILES = 'setup.cfg',
  ```
