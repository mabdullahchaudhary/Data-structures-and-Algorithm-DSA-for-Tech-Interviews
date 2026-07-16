

from functools import wraps

def log_activity(fun):
    @wraps(fun)
    def wrapper(*args,**kwargs):
        print(f"🚀Calling {fun.__name__}")
        result=fun(*args,**kwargs)
        print(f"✔ Calling {fun.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai(type):
    print(f"Brewing {type} chai")
    
brew_chai("Masala Chai")

