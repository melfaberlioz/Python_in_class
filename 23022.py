group = input('? ') # PMK-22, PMK-22s, PM-22 -> PMK-32, ...

course_index = group.index('-') + 1
new_course = int(group[course_index]) + 1
new_group = group[:course_index] + str(new_course) + group[course_index+1:]

print(new_group)