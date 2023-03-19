import functools

def do_twice(func):
    print("do twice run!")
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
       
        print("Before in wrapper")
        func(*args, **kwargs)
        
        print("After in wrapper")
    return wrapper

@do_twice
def say_whee(name):
    print(f"Hello! {name}")
    return "NAME: " + name

say_whee("Johny Wick")

print(say_whee)
help(say_whee)

"""
def decorator(func):
    def wrapper(name):
        print("Something happend before funcion is called")
        func(name)
        print("Something happend after funcitno is called")        
    return wrapper

@decorator
def say_whee(name):
    print(f"Hello! {name}")
    return "NAME: " + name

print(say_whee("John"))

def decorator(*args, **kwargs):
    
    def somewrapper(func):
        print("Some wrapper")
        print(func)
        return func
    return somewrapper


@decorator(param=1, param2=2)
def runner():
    print("Run forest run")
    
runner()

def decorator2(*args, **kwargs):
    
    def somewrapper(func):
        print("Some wrapper 2")
        func()
        return func
        
    return somewrapper


def runner2():
    print("Run forest run 2")
    
runner2 = decorator2(param1=123, param2=213)(runner2)
runner2()

"""