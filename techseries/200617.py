# Given hash table with courses with their corresponding prerequsite courses as keys
 # Return order of courses to take

def courses_to_take(course_to_prereqs):
  # Fill this in.
  completed = []
  result = []
  while courses:
    to_pop = []
    for course in courses:
      if all(c in completed for c in courses[course]) or not courses[course]:
        completed.append(course)
        to_pop.append(course)
    for tp in to_pop:
      courses.pop(tp)
      result.append(tp)
  return result
courses = {
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}
print courses_to_take(courses)
# ['CSC100', 'CSC200', 'CSC300']
