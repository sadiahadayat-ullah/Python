# Program: __enter__() and __exit__() Dunder Methods
# Description: Demonstrates how __enter__() and __exit__() manage
# entering and leaving a with statement.

class Demo:

    def __enter__(self):
        print('__enter__')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')

with Demo():
    print('Inside the with block')

