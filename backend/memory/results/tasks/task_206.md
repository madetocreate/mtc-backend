# Task 206

**Prompt:** logger = logging.getLogger(__name__)

**Result:**
The line of code you wrote is for Python, used to create or retrieve a logger object. `logging.getLogger(__name__)` creates a logger which is named after the module in which it is called. This logger is then used to create log messages that you can write to the console or a file.

Here is a bit more extended example of its usage:

```python
import logging

# create logger
logger = logging.getLogger(__name__)

# set level of logger
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
```
In this code, the logger will output log messages to the console as it has a StreamHandler (console handler). It also sets the minimum logging level to DEBUG, meaning all messages of level DEBUG and above will be logged. The messages will contain the timestamp, name of the logger, logging level, and the message, as defined in the formatter.
