import os

courses: list[str] = open("courses.txt", "r").read().splitlines()

year_search = input("enter the program level (1, 2, 3, 4): ")
suj_search = str.upper(input("enter the subject area (first 3 letters of the course code): "))

os.system('clear')
print(f"year {str(year_search)} {suj_search} courses:\n")

try:
  results: list[None] = [print(course) for course in courses if int(course[3]) == int(year_search) and suj_search in course]
  print(f"\n{len(results)} results from {len(courses)} courses")
except ValueError:
  print("please enter a year.")