from functools import wraps

def show_call(func):
    
    @wraps(func)
    def out (*args, **kwds):
        print(func.__name__, args, kwds)
        
        return func(*args, **kwds)
    return out

@show_call
def add(x, y):
    return x + y


add(4,3)