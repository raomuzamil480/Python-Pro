# Allow operater related to the class its self

class Student:
    count=0

    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.count +=1

    # instance method
    def get_info(self):
        print(f"{self.name} {self.age}")


    @classmethod
    def info(cls):
        return f"{cls.count}"

s=Student('name',21)
s=Student('name',21)
s=Student('name',21)
s.get_info()
print(Student.count)



#==========================================================
# with out class method
# class Student:
#     count=0
#
#     def info(self,name,gpa):
#         self.name=name
#         self.gpa=gpa
#         Student.count +=1
#         print(f"{self.name} and {self.gpa}")
# s=Student()
# s.info('rao',23.4)
# s.info('raosa',23.4)
# print(Student.count)