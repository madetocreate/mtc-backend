# Task 218

**Prompt:** logger.error("Es gab einen Fehler: " + str(e))

**Result:**
The code you just shared is written in Python, and it shows an example of how to log an error message in case an exception is caught. 

In this specific code snippet, the German text "Es gab einen Fehler:" translates to "There was an error:". The `str(e)` represents the error message that is associated with an exception `e`. It's converted to a string in order to be appended to the main error message. 

Keep in mind that `logger` should be defined beforehand (using `logging.getLogger()` for example) and `e` is usually obtained from `except` clause of try-except block like so:

```python
import logging

logger = logging.getLogger('my_logger')

try:
    # Some code that may raise an exception
except Exception as e:
    logger.error("Es gab einen Fehler: " + str(e))
```

This will output something like 
```shell
ERROR:my_logger:Es gab einen Fehler: description of error
``` 

Depending on your logging configuration.
