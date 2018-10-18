import sys

try:
    a+b
except Exception as e:
    print(sys.exc_info())