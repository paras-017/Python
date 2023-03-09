# Decorators --> Python decorators are a powerful and versatile tools that allow you to modify the behavior of functions and methods.They are a way to extend the functionality of a function or method without modifying its source code
def greet(fx):
    def mfx(*args, **kwargs):
        print('Good Morning')
        fx(*args, **kwargs)
        print('Thanks for using this function')
    return mfx

@greet
def hello():
    print('hello')

@greet
def sum(a,b):
    print(a+b)

sum(5,8)
# greet(hello)()
# greet(sum)(1,2)