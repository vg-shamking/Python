morning = ['Java', 'C', 'Ruby', 'Lisp', 'C#']
afternoon = ['Python', 'C#', 'Java', 'C', 'Ruby']

# possible_course = set(morning) ^ set(afternoon)
possible_course = set(morning).symmetric_difference(afternoon)
print(possible_course)

possible_courses = set(afternoon).symmetric_difference(morning)
print(possible_courses)
