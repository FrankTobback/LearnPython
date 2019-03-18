# Decorators can change the behaviour of functions

def cough_dec(func):

    def func_wrapper():
        #code before function
        print('*cough*')
        func()
        #code after function
        print('**cough')

    return func_wrapper

@cough_dec
def question():
    print('Can I get a discount?')

    
@cough_dec
def answer():
    print("It's only 50p you cheap fuck")


question()
answer()
