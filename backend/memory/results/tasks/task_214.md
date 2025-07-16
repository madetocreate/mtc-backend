# Task 214

**Prompt:** logger.info("Ein Task startet")

**Result:**
It looks like you are trying to use a logger in your code. Here's a simple way to initialize and use one in Python:

```python
import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Set level of logger
logger.setLevel(logging.INFO)

# Create handlers
console_handler = logging.StreamHandler()

# Create formatters and add it to handlers
console_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_format)

# Add handlers to the logger
logger.addHandler(console_handler)

logger.info('Ein Task startet')
```

This code will output a message "Ein Task startet" to the console. The logging level is set to INFO, so all messages of level INFO and above (WARNING, ERROR, CRITICAL) will be logged. 

Remember, it's a good practice to use a logger instead of simple print statements. It gives you a lot more flexibility and control over your log outputs. Depending on the configuration, you can direct these outputs to console, file or even over the network.
