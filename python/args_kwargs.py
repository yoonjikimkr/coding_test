def my_decorator(func):
    num2=7
    def inside(*args,**kwargs): # *args and **kwargs are used to pass a variable number of arguments to a function.
        ans=num2+func(*args,**kwargs) # *args is used to pass a non-keyworded, variable-length argument list.
        # **kwargs is used to pass a keyworded, variable-length argument list.
        return ans
    return inside(num2=4)
@my_decorator # @ is a decorator which is used to add some extra functionality to the function.
# @my_decorater function is to add 4 to the result of the function.
def central(num1,*args):
    return num1
print(central(5))