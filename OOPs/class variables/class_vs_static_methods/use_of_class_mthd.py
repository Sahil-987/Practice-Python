"""
ye sab kuch maine he soch kar likha h
"""


class Employee:

    sr_no = 1

    def __init__(self, name, age, department):
        self.sr_no = Employee.sr_no
        self.name = name
        self.age = age
        self.department = department
        Employee.set_srno()

    @classmethod #agar class method hata doge to error aayegi
    def set_srno(cls):
        cls.sr_no += 1

    
    



if __name__ == "__main__":
    emp1 = Employee("Sahil", 28, "AI")
    print(emp1.sr_no)
    emp2 = Employee("Waris", 24, "Developer")
    print(emp2.sr_no)
