# Task 204

**Prompt:** import logging

**Result:**
Sure, that's a good start. The `logging` module in Python is used to record (or log) events that happen when some software runs. The module provides you with functions and classes that you can use to add a logging system in your applications.

Typically, you could set up basic configurations for your logging system using `basicConfig(**kwargs)` method.

Here is an example:

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("This will get logged")
```

In this example, we set the level of logging to `INFO` which means the logger will handle all messages with a level of `INFO` and above (in severity).

Then, we log the phrase "This will get logged". The `INFO` level means the information under this level confirms that things are working as expected.

Remember that there are several levels of logging like `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`. You can choose one depending on your needs.
