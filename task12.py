students = [
  {"name": "Aziz", "grade": 89},
  {"name": "Kamola", "grade": 95},
  {"name": "Javlon", "grade": 76}
]

natija = sorted(map(lambda student: student['grade'], students))

print(natija)
