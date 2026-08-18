def check_access(function):

    def wrapper(is_allowed):
        if is_allowed:
            function()
        else:
            print("Access denied.")
    return wrapper

@check_access
def secret_page():
    print("Welcome to secret page.")

secret_page(True)
secret_page(False)
