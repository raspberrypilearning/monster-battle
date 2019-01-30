def list_args(*args):
    print('Printing args:')
    for a in args:
        print(a)

list_args(1,2)
list_args(1,2,3,4,5)

def list_kwargs(**kwargs):
    print('Printing kwargs:')
    for key, value in kwargs.items():
        print(key, value)

list_kwargs(name='rik')
list_kwargs(name='rik', age='too old')
