# FOR LOOPS

# ninjas = ['Ryu','crystal','yoshi','ken']
#
# # for ninja in ninjas:
# #     print(ninja)
#
# # for ninja in ninjas[1:3]:
# #     print(ninja)
#
# for ninja in ninjas:
#     if ninja == 'yoshi':
#         print(f'{ninja} - black belt')
#         #BREAK stops the loop from cycling trough the rest of the list
#         break
#     else:
#         print(ninja)

# WHILE LOOPS
age = 25
num = 0

while num < age:
    if num == 0:
        num += 1
        continue
    if num % 2 == 0:
        print(num)
    if num > 10:
        break
    num += 1
