# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {function(args[0], args[1], args[2])}")
    return wrapper


# Use the decorator 👇
@logging_decorator
def a_function(x, y, z):
    return x + y + z


a_function(1, 2, 3)


