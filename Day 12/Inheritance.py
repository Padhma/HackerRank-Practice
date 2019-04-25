class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
   
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    def calculate(self):
        avg = sum(self.scores)/len(self.scores)
        if avg > 89:
            return 'O'
        if avg > 79:
            return 'E'
        if avg > 69:
            return 'A'
        if avg > 54:
            return 'P'
        if avg > 39:
            return 'D'
        else:
            return 'T'
        

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) 
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())