student={'name':'xxx','age':18,'city':'chennai','dept':'cs'}
print(student.copy()) #copy()
x=dict.fromkeys(student) #fromkeys()
print(x)
student['name']='yyy' #update()
print(student.get('name')) #get()
student.pop('city') #pop()
print(student)
print(student.items()) #items()
print(student.keys()) #keys()
print(student.values()) #values()
print(student.popitem()) #popitem()
y=student.setdefault('age') #setdefault
print(y)
print(student.clear()) #clear()


