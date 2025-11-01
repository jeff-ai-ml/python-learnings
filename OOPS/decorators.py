



def my_decoration(func):
    def wrapper(*args,**kwargs):
        print("This is executed before functon call")
        result = func(*args,**kwargs)
        print("This is executed after function call")
        return result
    return wrapper




@my_decoration
def add(a,b):
    print(f"Addition of A and B is {a+b}")
    return a+b

@my_decoration
def sub(a,b):
    print(f"Addition of A and B is {a-b}")
    return a+b



add(100,202)
sub(100,202)

