class User:
    def __init__(self, name,fname,age,contact,adress):
        self.name = name
        self.fname = fname
        self.age= age
        self.contact= contact
        self.adress= adress
        def registerUser(self):
            print( self.name)
            print(self.fname)
            print(self.age)
            print(self.contact)
            print(self.adress)



class Teacher(User):
    def __init__(self,name,fname,age,contact,adress,classAssigned, subject,qualification ):
          super().__init__(self,name,fname,age,contact,adress)
          self.classAssigned=classAssigned
          self.subject=subject
          self.qualification=qualification

    def registerUser(self):
        super().registerUser()
        print(self.classAssigned)
        print(self.qualification)
        print(self.subject)

class Student(User):
    def __init__(self, name, fname, age, contact, adress, classEnrolled, subject, Program):
        super().__init__(self, name, fname, age, contact, adress)
        self.classEnrolled = classEnrolled
        self.subject = subject
        self.Program = Program

    def registerUser(self):
        super().registerUser()
        print(self.classEnrolled)
        print(self.Program)
        print(self.subject)

class Admin(User):
    def __init__(self, name, fname, age, contact, adress, role, dept, level):
        super().__init__(self, name, fname, age, contact, adress)
        self.role = role
        self.dept = dept
        self.level = level

    def registerUser(self):
        super().registerUser()
        print(self.level)
        print(self.dept)
        print(self.role)