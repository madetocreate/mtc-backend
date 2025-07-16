# Task 205

**Prompt:** import datetime

**Result:**
Sure, I can assist you with that. With `datetime`, you can handle dates and time in your python programs.

Here is an example of how you can use it:

```python
import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()
print(current_datetime)

# Outputs something like this: 2021-10-22 13:52:30.813342

# Get today's date
today = datetime.date.today()
print(today)

# Outputs something like this: 2021-10-22
```

In this example, `datetime.datetime.now()` gives you the current date and time. `datetime.date.today()` returns the current date. You can extract more specific information like year, month, day, hour, minute, second, etc. from the datetime object.

With datetime module, you can also perform various operations like comparing two dates/times, calculating the difference between dates/times, etc.
