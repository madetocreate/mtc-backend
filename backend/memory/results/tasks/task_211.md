# Task 211

**Prompt:** logger.addHandler(handler)

**Result:**
Your statement is a part of how to configure a logger in Python. It's a method to add specific handler to the logger object. Logging handlers send the log records (created by the developers) to the appropriate destination. 

Here is an example of how to use it properly:

```python
import logging

# Create a logger object.
logger = logging.getLogger(__name__)

# Create a handler object.
handler = logging.StreamHandler()

# add formatter if you want to customize the log message's format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger.
logger.addHandler(handler)

# Set the priority level. Log everything including and above INFO.
logger.setLevel(logging.INFO)

# Now we can log messages.
logger.info('This is an INFO message.')
```

In the above program, we are first creating a logger object. Then we create a handler which, in this case, is a `StreamHandler` that logs the message to the console. Then, we set a format for our logs and add this formatter to our handler. We add this handler to our logger, set a level of logging (in this case, to INFO) then log a message. 

Make sure you set appropriate logging level for both logger and handler. The logger and handler have their own levels. The logger's level is set with `logger.setLevel()` and handler’s level with `handler.setLevel()`. The effective level of a logger is computed with respect to the hierarchy. That is, it will emit a log if either the logger's level or the handler's level is satisfied.
