# decorator use add extra functionality with out change the code in function
def admin_only(func):
    def wrapper():
        role = "user"

        if role == "admin":
            func()
        else:
            print("Access denied")

    return wrapper


@admin_only
def delete_user():
    print("User deleted")

delete_user()

#=========================================
def validate(func):
    def wrapper(age):
        if age < 0:
            print("Invalid age")
        else:
            func(age)
    return wrapper


@validate
def register(age):
    print("Registered")

register(20)
 #=======================================
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper

@my_decorator
def ok(name):
    print( f"My name is {name}")
ok('Rao Muzamil')