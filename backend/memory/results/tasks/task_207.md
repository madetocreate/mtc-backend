# Task 207

**Prompt:** handler = logging.FileHandler('my_app.log')

**Result:**
It seems like you're trying to create a file handler for your logger in python. Below is an example of how you can create a LOGGER with your `handler`:

```python
import logging

# Create a logger
logger = logging.getLogger(__name__)

# Set the level to logging.INFO to record all logs from INFO level and up
logger.setLevel(logging.INFO)

# Create a handler for the logger
handler = logging.FileHandler('my_app.log')

# Create a Formatter for our handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Assign the Formatter to the Handler
handler.setFormatter(formatter)

# Add the Handler to our Logger
logger.addHandler(handler)
```

Now you can use this logger to log messages to your specified file (`my_app.log`) like so:

```python
logger.info('This is an info message.')
logger.warning('This is a warning message.')
logger.error('This is an error message.')
```
