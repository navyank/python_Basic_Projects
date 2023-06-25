student={"name":"kiran",
         "age":25,
         "mark1":76,
         "mark2":99}
print(student["name"])
print(student.get("name"))
print(student.keys())
print(student.values())

student["name"]="Manu"
student["phone"]=7592916929
print(student)
student.update({"name":"Mohan"})#############update is used to add or modify remainig dictionary
student.update({"Address":"Kottayam"})
print(student)
student.pop("name")
print(student)
student.popitem()
print(student)
# del student["name"]#########name is already pop
# print(student)
# del student
# student.clear()
candidate=student.copy()###this line 24 and 26 are same
print(candidate)
candidate=dict(student) 
print(candidate)
