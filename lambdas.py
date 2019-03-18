# lambdas are kind of anonymous functions, used for functions that you only use once

nums = [1,2,3,4,5,6]

# #normal function
# def square(n):
#     return n*n
#
# print(list(map(square, nums)))

#Lambda method
# if you want to pass in mutliple arguments , just comma seperate them => Ex. lambda n,x: n*n
print(list(map(lambda n: n*n, nums)))
