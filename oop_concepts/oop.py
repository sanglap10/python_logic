class Student:
    def set_name(self,name):
        self.name = name 

    def get_name(self):
        return self.name

stu = Student()
stu.set_name("bhaskar")
print(stu.get_name())