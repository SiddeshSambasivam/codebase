# **A breif summary of the Logging Module**

Logging errors, outputs are a essential part to debug any program and the `logging` module provides an integrated module to log all sorts of instances that occur in a program.

```python
# Import logging module
import logging

# Different severities
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# Configuring the output of the logger
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.warning('This will get logged to a file')


```

Logging module has something called a `logger` which could be used to log messages. And has 5 default levels of severity.

```bash

$ WARNING:root:This is a warning message
$ ERROR:root:This is an error message
$ CRITICAL:root:This is a critical message

```

- The format of the output shows the level, name, and message separated by a colon (:), is the default output format that can be configured to include things like timestamp, line number, and other details.
