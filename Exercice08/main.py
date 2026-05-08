def log_decorator(func):
     def wrapper():
         print("Début")
         func()
         print("Fin")
     return wrapper
 
@log_decorator
def function_test():
    """Fonction sans arguments"""
    print("Cette fonction ne prend pas d'arguments.")

@log_decorator
def function_t():
    print("T")


function_test()
function_t()




