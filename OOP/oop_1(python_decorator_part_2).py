def get_function_name_dec(func):
    def wrapper(*arg):
        function_returns = func(*arg) #What our function returns
        return func.__name__+":"+function_returns

    return wrapper

@get_function_name_dec
def hello_world():
  return "Hi"

print(hello_world())
