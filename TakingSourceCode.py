import inspect
import sys


testing = (sys._getframe().f_back.f_code)
lines = inspect.getsourcelines(testing)
print("".join(lines[0]))
