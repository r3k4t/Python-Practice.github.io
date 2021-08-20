
# orig_func already given
def orig_func():
    print("Wheee!")

 # write decorator
def my_decorator(some_function):
   def my_wrapper():
       print("do something before ")
       some_function()
       print("do something after")

   return my_wrapper


# create decorator and call  orig func
orig_func = my_decorator(orig_func) # craete decorator,modify functioning
orig_func() # call modified orig_func
