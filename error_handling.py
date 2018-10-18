import sys

try:
    a+b
except Exception as e:

    print('Error: {}, {}. line: {}'.format(sys.exc_info()[0],
                                           sys.exc_info()[1],
                                           sys.exc_info()[2].tb_lineno))