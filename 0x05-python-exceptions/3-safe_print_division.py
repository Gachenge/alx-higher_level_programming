def safe_print_division(a, b):
    c = 0
    try:
        c = a / b
    except (ZeroDivisionError, TypeError):
        c = None
    finally:
        print("Inside result: {}".format(c))
        return c
