# Task 209

**Prompt:** formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

**Result:**
The line of code you have provided is for creating a formatter object in Python's logging module. The logging module is useful for tracking or debugging code.

Let's break down the format of the formatter:

- '%(asctime)s' : This will be replaced by the time of creation of the LogRecord.
- '%(levelname)s' : This will be replaced by the text representation of the log level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
- '%(message)s' : This is your actual log message.

You can use the formatter object to set a format for the handler:

```python
handler = logging.StreamHandler()  # Use whatever handler you want here
handler.setFormatter(formatter) 

logger = logging.getLogger(__name__)
logger.addHandler(handler)
```
Now, whenever you log a message, it will be displayed in the format you set. For example:
```python
logger.error('This is an error message')
```
Will output (assuming this was run on Jan 1, 2000 at exactly midnight):
```
2000-01-01 00:00:00,000 - ERROR - This is an error message
```
