def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local:", spam)
    do_nonlocal()
    print("After nonlocal:", spam)

scope_test()
print("In global scope:", spam)
