#You have a function that prints a message:

def say_hello():
    print("Hello")

#Now, you want to:

#Add stars before and after it like this:

# ****
# Hello
# ****


# You don’t change the original say_hello() function.
# Instead, you wrap it using a decorator

#make the decorator
def star_decorator(func):
    def wrapper():
        print("****")
        func()
        print("****")
    return wrapper


#Now, decorate your function:
@star_decorator
def say_hello():
    print("Hello")


say_hello()
