groupmates = [
	{
		"name": ("Emin"),
		"group": "1702",
		"age": 19,
		"marks": [4, 3, 3, 5, 4]
	},
	{
		"name": ("Maxim"),
		"group": "1702",
		"age": 20,
		"marks": [4, 5, 3, 4, 3]
	},
	{
		"name": ("Polina"),
		"group": "1702",
		"age": 19,
		"marks": [5, 5, 5, 5, 5]
	},
	{
		"name": ("Seinur"),
		"group": "1701",
		"age": 20,
		"marks": [4, 4, 5, 5, 5]
	}
	]

def print_students(students):
	print (("Student Name").ljust(15),	\
		("Student Group").ljust(8),	\
		("Student Age").ljust(8),	\
		("Studetn Marks").ljust(20))
	for student in students:
		print (student["name"].ljust(15),	\
			student["group"].ljust(8),	\
			str(student["age"]).ljust(8),	\
			str(student["marks"]).ljust(20))
	print ("\n")
print_students(groupmates)

def students_avg(students, n):
   
 
    return [s for s in students if sum(s['marks'])/len(s['marks']) > n]
 

print()
print_students(students_avg(groupmates, 3))
