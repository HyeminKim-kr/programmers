N = int(input())
students = []

for _ in range(N):
    name, korean, english, math = input().split()
    korean = int(korean)
    english = int(english)
    math = int(math)
    students.append((name, korean, english, math))
    
students.sort(key=lambda students: (-students[1], students[2], -students[3], students[0]))

for student in students:
    print(student[0])
    