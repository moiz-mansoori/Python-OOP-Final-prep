# Basic Decorator
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")      
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()



# Decorator with Arguments:

# def repeat(num_times):
#     def decorator_repeat(func):
#         def wrapper(name):
#             for _ in range(num_times):
#                 func(name)
#         return wrapper
#     return decorator_repeat

# @repeat(num_times=3)
# def greet(name):
#     print(f"Hello {name}")

# greet("Moiz")




# Class Decorator:

# class DecoratorClass:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, name):
#         print("Something is happening before the function is called.")
#         self.func(name)
#         print("Something is happening after the function is called.")

# @DecoratorClass
# def say_hello(name):
#     print(f"Hello {name}!")

# say_hello("Mansoori")




# Uppercase Decorator:

# def uppercase_decorator(func):
#     def wrapper(name):
#         result = func(name)
#         return result.upper()
#     return wrapper

# @uppercase_decorator
# def say_hello(name):
#     return f"Hello {name}!"

# print(say_hello("world"))


 # lowercase_decorator
 
# def lowercase_decorator(func):
#     def wrapper(name):
#         result = func(name)
#         return result.lower()
#     return wrapper

# @lowercase_decorator
# def say_hello(name):
#     return f"Hello {name}!"

# print(say_hello("WORLD"))




# def wrap_result_in_html_tags(tag):
#     def decorator(func):
#         def wrapper():
#             return f"<{tag}>{func()}</{tag}>"
#         return wrapper
#     return decorator

# @wrap_result_in_html_tags("b")
# def my_function():
#     return "Hello, world!"

# my_function()


def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def make_italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@make_bold
@make_italic
def say_hello():
    return "Hello World!"

print(say_hello())
