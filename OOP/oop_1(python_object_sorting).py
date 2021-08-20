# JavaScript OOP Technique

'''
# Javascript program Class
class Employee {
    constructor(name,dept,age){
	  this.name = name
	  this.dept = dept
	  this.age = age
	}
}
'''
# python program Class
class Employee:
     # function
	 def __init__(self,name,dept,age):
		 self.name = name
		 self.dept = dept
		 self.age = age
     # function
	 def __repr__(self):
		 return '{' + self.name + ', ' + self.dept + ', ' + str(self.age) + '}'


# javascript program : (emp = new Employee())
# python program: (emp=[Employee()])
emp = [Employee('John','IT',28),
	   Employee('Rohan','Banking',27),
	   Employee('Johny','Finance',26),
	   Employee('Alex','Font-End Engineer',20),
	   Employee('Bravo','Back-End Engineer',21),
	   Employee('Charlos','IT Manager',23),
	   Employee('Tusar','Senior Software Engineer',23)]


# javascript program:console.log()
# python program:print()
print(sorted(emp,key=lambda x: x.name))
print(sorted(emp,key=lambda x: x.name,reverse=True))
