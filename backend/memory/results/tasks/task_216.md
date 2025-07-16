# Task 216

**Prompt:** logger.info("Ein Task endet")

**Result:**
Your sentence looks like it could fit into a Python logging structure. In Python, logging is an essential part of the code, used for tracing code execution and debugging. If you would like to log an info message "Ein Task endet", it'd look like this:

```python
import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Set level of logger
logger.setLevel(logging.INFO)

# Create handlers
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

# Create formatters and add it to handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(handler)

# Log the info message
logger.info('Ein Task endet')
```

This Python code sets up a basic logger, which will log the message "Ein Task endet" at the INFO log level. The logger output will include the current timestamp, logger name, level of the log, and the log message.

You can customize levels, handlers, formatters based on your need.
