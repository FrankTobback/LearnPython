grades = ['A', 'B', 'C', 'F','A','F']

def remove_fails(grade):
    return grade != 'F'

#print(list(filter(remove_fails, grades)))

# For loop method

# filtered_grades = []
# for grade in grades:
#     if grade != 'F':
#         filtered_grades.append(grade)
#
# print(filtered_grades)


# comprehension method
print([grade for grade in grades if grade != 'F'])     
