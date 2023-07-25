# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# print_kwargs(name='John', age=30, city='New York')

# def print_args_and_kwargs(*args, **kwargs):
#     print("Positional arguments:")
#     for arg in args:
#         print(arg)
#
#     print("\nKeyword arguments:")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# print_args_and_kwargs(1, 2, 3, name='John', age=30, city='New York')

def arbitrary_args_function(*args):
    for arg in args:
        print(arg)

arbitrary_args_function(1, 2, 3)  # Output: 1 2 3
arbitrary_args_function('apple', 'banana', 'orange')  # Output: apple banana orange
