"""
mocking is useful when
- you dont have access to the modules you want to use
- some function produces sensitive data
- a function takes very long time
- a function requires an internet connection
- a function requires a database connection
  (e.g. replace the real database by a smaller test database (sqlite))
- a function produces random results
"""
import math
from unittest.mock import patch

with patch('math.sin', return_value=42):
    print(math.sin(123))

print(math.sin(123))
