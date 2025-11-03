

def my_decor(func):
    def wrapper(*arg,**kwarg):
        print("This is before function call")
        result = func(*arg,**kwarg)
        print("This is after function call")
        return result
    return wrapper




@my_decor
def add(a,b):
    print(f"Addition of {a} and {b} is {a+b}")
    return a+b


add(5,3)
