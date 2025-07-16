# Task 208

**Prompt:** handler.setLevel(logging.INFO)

**Result:**
Your code snippet suggests that you're using Python's built-in logging module to log messages with a level of INFO or higher. However, your code alone wouldn't work as it lacks context. A correct setup would look like this:

```python
import logging

# Create or get the logger
logger = logging.getLogger(__name__)  

# set log level
logger.setLevel(logging.INFO)

# create console handler and set level to info
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to handler
handler.setFormatter(formatter)

# add handler to logger
logger.addHandler(handler)

# now you can use logger anywhere in your script
logger.info('This is an info message')
```

This code sets up logging to output to the console and to format the log messages to include the timestamp, script name, level name and the actual message. It logs any messages with a severity level of INFO or above.
