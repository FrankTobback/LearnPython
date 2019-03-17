my_name = 'frank'

def print_name():
    # overwrite a global variable from inside a function use GLOBAL
    global my_name
    my_name = 'vegeta'
    print('the name inside the function is', my_name)

print_name( )
print('outside the function the name is', my_name)
